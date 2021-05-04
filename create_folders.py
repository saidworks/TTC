import os

#path
path = './'

#create lists
folders = ['chapter'+str(i) for i in range(1,25,1)]

#make directories
for folder in folders:
    os.makedirs(os.path.join(path,folder))
