import os

#get directory name
dirname=input("Enter the directory: ")
#create a list
os.chdir(dirname)
dirlist=os.listdir()
#get new lead name
lead=input("What label do you want for the pictures? ")
picture_number=1
#rename pictures
for filename in dirlist:
    if filename.endswith('.jpg'):
        newname = lead + str(picture_number)+".jpg"
        os.rename(filename,newname)
        picture_number +=1
