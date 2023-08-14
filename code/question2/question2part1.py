# -*- coding: utf-8 -*-
"""question2part1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yDVR_CHUftJilUaIPqEjP-G-qWQQ4Exl
"""

from google.colab import files
uploaded = files.upload()
import pandas as pd

data = pd.read_csv("Dataset.csv")
import random
import numpy as np 
col=['F1','F2']
data = pd.read_csv("Dataset.csv",names=col)
numm=data.to_numpy()
# random initialization
z=[]
e=[]
n=1000
for i in range(n):
    z.append(random.randint(0,3))
#print(z)
data['Z']=z
numm=data.to_numpy()

def random_initialization():
  z=[]
  for i in range(1000):
    z.append(random.randint(0,3))
  data['Z']=z
  return z

def Pointscount(z):
  count={}
  for i in z:
    if i in count:
      count[i]=count[i]+1
    else:
      count[i]=1
  return count

def k_means():
 
  while(True):
    # mean calculation 
    currentmean={}
    for i in  range(1000):
      xi=np.copy(numm[i,:2])
      if numm[i][2] in currentmean:
        currentmean[numm[i][2]]=currentmean[numm[i][2]]+xi
      else:
        currentmean[numm[i][2]]=xi
    count=Pointscount(numm[:,2])
    for i in count:
      if(count[i]!=0):
        currentmean[i]=currentmean[i]/count[i]
    
    flag=0

    # reinitialization 
    error=0

    for i in range(1000):
      xi=np.copy(numm[i,:2])
      k=arg=numm[i][2]
      dist = (np.linalg.norm(xi- currentmean[arg]))**2
      error=error+dist
      for j in currentmean:
        val = (np.linalg.norm(xi-currentmean[j]))**2
        if(val<dist):
          k=j
          dist=val
      if(k!=arg):
        flag=1
        numm[i][2]=k
    #print(error)
    e.append(error)

      
    count=Pointscount(numm[:,2])
    if(flag==0):
      return e
      break

def plot_kmeans(y):

  x=np.arange(1,len(e)+1,1)
  plt.plot(x, y,'-ok')
  plt.title("Error Function VS No of iteration")
  plt.xlabel("No of Iteration")
  plt.ylabel("Error function")
  plt.show()

  final=pd.DataFrame(numm,columns=['F1','F2','Z'])
  
  plt.scatter( final['F1'][(final.Z == 0)],final['F2'][(final.Z == 0)],marker='o',color='black',label='cluster4')
  plt.scatter( final['F1'][(final.Z == 1)],final['F2'][(final.Z == 1)],marker='o',color='red',label='cluster1')
  plt.scatter( final['F1'][(final.Z == 2)],final['F2'][(final.Z == 2)],marker='o',color='blue',label='cluster2')
  plt.scatter( final['F1'][(final.Z == 3)],final['F2'][(final.Z == 3)],marker='o',color='indigo',label='cluster3')
  
  plt.xlabel('Feature 1')
  plt.ylabel('Feature 2')
  plt.legend(bbox_to_anchor = (1.05, 0.6))

import matplotlib.pyplot as plt
z=random_initialization()
#print(z)
numm=data.to_numpy()
e=[]
e=k_means()
y=np.array(e)
plot_kmeans(y)

z=random_initialization()
numm=data.to_numpy()
e=[]
e=k_means()
y=np.array(e)
plot_kmeans(y)

z=random_initialization()
numm=data.to_numpy()
e=[]
e=k_means()
y=np.array(e)
plot_kmeans(y)

z=random_initialization()
numm=data.to_numpy()
e=[]
e=k_means()
y=np.array(e)
plot_kmeans(y)

z=random_initialization()
numm=data.to_numpy()
e=[]
e=k_means()
y=np.array(e)
plot_kmeans(y)