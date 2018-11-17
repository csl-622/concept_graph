import os

folder = 'processed/'

Files = sorted(os.listdir(folder))

n = len(Files)
m = n//6

for i in range(6):
	x = i*m
	y = x + m
	for j in range(x,y):
		os.system('scp ' + folder + Files[j] + ' ' + '../run' + str(i+1) + '/processed/' + Files[j])
