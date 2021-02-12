import os 
path = 'E:/GLDAS/2013'
os.chdir(path)
for i in range (1,13):
    Newfolder =str(i)
    os.makedirs(Newfolder)
#C:\Users\bikra\Desktop\Modis classif