from mpl_toolkits.mplot3d import Axes3D
import os
import matplotlib.pyplot as plt
import networkx as nx
import nltk
a = 0


def knowledge_graph(G):    
    label=nx.get_node_attributes(G,'label')
    
    
    node_name = {}
    for i in label:
        node_name[label[i]] = i
    
    return node_name

def plot_pre_post3D(degree_list,kj):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x = []
    y = []
    z = []
    
    k=1
    for key,value in degree_list.items():
        x.append(k)
        y.append(degree_list[key][0])
        z.append(degree_list[key][1])
        k+=1
    
    ax.scatter(x, y, z, c='r', marker='o')
    
    ax.set_xlabel('Words in sequence')
    ax.set_ylabel('predegree')
    ax.set_zlabel('postdegree')
    if not os.path.exists('output_plot'):
        os.makedirs('output_plot')
    plt.savefig('output_plot/degree_graph'+str(kj)+'.png',dpi=400) 
    plt.close()    

def plot_degree_seq(degree_list, kj):
    
    fig = plt.figure()
    sc = []
    x = []
    y = []
    z = []
    s = []

    k = 1
    for key,value in degree_list.items():
        x.append(k)
        y.append(degree_list[key][0])
        z.append(degree_list[key][1])
        s.append(degree_list[key][2])
        sc.append(1)
        k+=1
    
    plt.scatter(x,y,c='r',s=sc,label='pre-degree sequence')
    plt.scatter(x,z,c='y',s=sc,label='post-degree sequence')
    plt.scatter(x,s,c='b',s=sc,label='global-degree sequence')
    plt.legend()
    plt.savefig('degree_plot/plot'+str(kj)+'.png',dpi=800)
    plt.close()


def plot_final_degree(final_degree_list):
    maxNum = 0
    for i in range(1,len(final_degree_list)):
        if(len(final_degree_list[i]) > len(final_degree_list[i-1])):
            maxNum = i
    
    x = [0]*len(final_degree_list[maxNum])
    avgPreDeg = [0]*len(final_degree_list[maxNum])
    avgPostDeg = [0]*len(final_degree_list[maxNum])
    avgGlobalDeg = [0]*len(final_degree_list[maxNum])
    sc = []
    
    for i in range(len(x)):
        for k in range(len(final_degree_list)):
            if(final_degree_list[k].get(i) != None):
                avgPreDeg[i]+=final_degree_list[k][i][0]               
                avgPostDeg[i]+=final_degree_list[k][i][1]
                avgGlobalDeg[i]+=final_degree_list[k][i][2]
        x[i]=i
        sc.append(1)
    
        
    avgPreDeg = [f/len(final_degree_list)  for f in avgPreDeg]
    avgPostDeg = [f/len(final_degree_list)  for f in avgPostDeg]
    avgGlobalDeg = [f/len(final_degree_list)  for f in avgGlobalDeg]
    
    print(avgPreDeg)
    plt.scatter(x,avgPreDeg,c='r',s=sc,label='average pre-degree sequence')
    plt.scatter(x,avgPostDeg,c='y',s=sc,label='average post-degree sequence')
    plt.scatter(x,avgGlobalDeg,c='b',s=sc,label='average global-degree sequence')
    plt.legend()
    plt.savefig('plotAvg.png',dpi=800)
    plt.close()    
    
    
    
        
def network_analysis():
    G = nx.read_graphml('outputGraph.graphml')
    nodeId = nx.get_node_attributes(G,'label')
    node_name = knowledge_graph(G)
    
    files = os.listdir("test_doc")
    #files = ['federalist_1.txt']
    kj = 1
    final_degree_list = []
    for file in files:
            
        with open("test_doc/"+file,'r') as f:
            raw = f.read()
            tokens = nltk.word_tokenize(raw)
            text = nltk.Text(tokens)
            
            en_stop = set(nltk.corpus.stopwords.words('english'))
            text = [token.lower() for token in text if token not in en_stop]
            
            H = nx.Graph()
            
            degree_list = {}        
            flag = 0
            nodesHIdList = []
            degreeIndex = 0
            for i in text:
                nodesHIdList = H.nodes()
                
                if(flag==0):
                    if(node_name.get(i) != None):
                        H.add_node(i)
                        global_deg = G.degree(node_name[i])
                        degree_list[degreeIndex] = [0,0,global_deg,i]
                        degreeIndex+=1
                    else:
                        continue
                    
                    flag = 1
                else:
                    if(node_name.get(i) != None):
                        
                        node_id = node_name[i]
                        H.add_node(i)
                        neighbor_list = G.neighbors(node_id)
                        for node in neighbor_list:
                            if(nodeId[node] in nodesHIdList):                    
                                H.add_edge(i,nodeId[node])
                        pre = H.degree(i)
                        global_deg = G.degree(node_name[i])
                        degree_list[degreeIndex] = [pre,0,global_deg,i] # [pre,post,global]                    
                        degreeIndex+=1
            
                               
            for key, value in degree_list.items():
                degree_list[key][1] = H.degree(degree_list[key][3]) - degree_list[key][0]
                
            
            plot_pre_post3D(degree_list,kj)
            plot_degree_seq(degree_list, kj)
            
            
        final_degree_list.append(degree_list)
        kj+=1
    
    plot_final_degree(final_degree_list)
'''
if not os.path.exists('graphs'):
    os.makedirs('graphs')
nx.write_gexf(H, "graphs/graphH"+str(kj)+".gexf")

'''