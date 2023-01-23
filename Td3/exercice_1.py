import os

def find(directory): 
    lst = []
    for (root,dir,files) in os.walk(directory,topdown=True):
        for name in files:
            lst.append(os.path.join(root,name))
    print("\n".join(lst))

def findcount(directory): 
    countfile,countdir,countlink=0,0,0
    for (root,dir,files) in os.walk(directory,topdown=True):
        for name in files:
            countfile +=1
            if(os.path.islink(os.path.join(root,name))):
                countlink+=1
        for name in dir:
            countdir +=1
            if(os.path.islink(name)):
                countlink+=1
    print(str(countfile)+"\n"+str(countdir)+"\n"+str(countlink))

def findproperties(directory): 
    nbpublic,nbprivate=0,0
    for (root,dir,files) in os.walk(directory,topdown=True):
        for name in files:
            if os.lstat(os.path.join(root,name)).st_mode%64==0:
                nbprivate+=1     
            else :
                nbpublic+=1
        for name in dir:
            if os.lstat(os.path.join(root,name)).st_mode%64==0:
                nbprivate+=1     
            else :
                nbpublic+=1

    print("repetoires ou fichers privés : "+str(nbprivate)+"\nrepertoires ou fichiers publics : "+str(nbpublic))


#src="./tests/Boulot/patron.txt"
#dst="./tests/shortcuts.txt"
#os.symlink(src,dst)
#src="./tests/Boulot"
#dst="./tests/shortcutdir"
#os.symlink(src,dst)
find("tests")
print("---")
find(".")
print("---")
findcount("tests")
print("---")
findcount(".")
print("---")
findproperties("tests")

