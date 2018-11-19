import os

for i in range(2,25):
	os.system('scp -r run1/ ' + 'run' + str(i) + '/')
