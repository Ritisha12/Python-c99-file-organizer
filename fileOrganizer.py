import shutil
import os

mypath = input("Enter the name of the directory to be sorted")
# list of all the files in the directory
list_of_files = os.listdir(mypath)

for file in list_of_files:
    name,ext = os.path.splitext(file)
    print(name + ext)
    extn = ext[1:]
    
    if extn == '':
        continue
    if os.path.exists(mypath+'/'+extn):
        shutil.move(mypath+'/'+file,mypath+'/'+extn+'/'+file)
    else:
        os.makedirs(mypath+'/'+extn)
        shutil.move(mypath+'/'+file,mypath+'/'+extn+'/'+file)