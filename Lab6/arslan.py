import os
def list(path):
    all=os.listdir(path)
    directories=[]
    files=[]
    for i in all:
        if os.path.isdir(path+"/"+i):
            directories.append(i)
        else:
            files.append(i)
    print("Directories:", directories)
    print("Files:", files)
    print("All:", all)
list(".")