import os 
path = 'E:/GLDAS/2013' #specify path
os.chdir(path)
for i in range (1,13):
    Newfolder =str(i) 
    os.makedirs(Newfolder) #create new folders
