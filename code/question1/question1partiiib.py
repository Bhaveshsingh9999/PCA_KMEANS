# -*- coding: utf-8 -*-
"""question1partiiib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZHK5GacfhqqEUzfEYsqX3VZfCp0TUgUe
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import numpy as np
from numpy.linalg import eig
import matplotlib.pyplot as plt
import math
col=['F1','F2']
data = pd.read_csv("Dataset.csv",names=col)
numm=data.to_numpy()

def transpose(matrixa):
  matrixb=np.zeros((2,1000))
  for i in range(2):
    for j in range(1000):
      matrixb[i][j]=matrixa[j][i]
  return matrixb

def radial_kernelmatrix(matrixa,sigma):
  k=np.zeros((1000,1000))
  temp=np.zeros((2,2))
  for i in range (1000):
    for j in range(1000):
      temp=matrixa[i]-matrixa[j]
      k[i][j]=np.dot(temp,temp)
      k[i][j]=k[i][j]/(2*(sigma**2))
      k[i][j]=math.exp(k[i][j]*-1)

  return k

def centering(matrixk):
  i=np.identity(1000)
  x=np.ones((1000,1000))/1000
  t=i-x
  kc=np.matmul(t,matrixk)
  kc=np.matmul(kc,t)
  return kc

def plotpca(pjojectedmatrix,title):
  final = pd.DataFrame(pjojectedmatrix,columns=['F1','F2'])
  final.plot(kind = 'scatter',x = 'F1',y = 'F2',color = 'red')
  plt.xlabel('principal component 1')
  plt.ylabel('principal component 2')
  plt.grid()
  plt.title(title)
  plt.show()

def kernel_pca(numm,sigma,title):
  kmatrix=radial_kernelmatrix(np.copy(numm),sigma)
  kcentered=centering(np.copy(kmatrix))
  eigenvalues,eigenvectors=eig(kcentered)
  idx=eigenvalues.argsort()[::-1]
  eigenvalues=eigenvalues[idx]
  eigenvectors=eigenvectors[:,idx]
  sum=0
  for i in eigenvalues:
    sum=sum+i
  print(" total sum is ",sum)
  lambda1=eigenvalues[0]
  lambda2=eigenvalues[1]
  print("information capture by the top 2 eigen vector ",((lambda1+lambda2)*100)/sum,"%")
  m=eigenvectors[:,:2]
  m[:,0]=m[:,0]/math.sqrt(lambda1)
  m[:,1]=m[:,1]/math.sqrt(lambda2)
  final2=np.matmul(kcentered,m)
  plotpca(np.copy(final2),title)

kernel_pca(np.copy(numm),0.1,'Radial basis sigma = 0.1')

kernel_pca(np.copy(numm),0.2,'Radial basis sigma = 0.2')

kernel_pca(np.copy(numm),0.3,'Radial basis sigma = 0.3')

kernel_pca(np.copy(numm),0.4,'Radial basis sigma=0.4')

kernel_pca(np.copy(numm),0.5,'Radial basis sigma = 0.5')

kernel_pca(np.copy(numm),0.6,'Radial basis sigma = 0.6')

kernel_pca(np.copy(numm),0.7,'Radial basis sigma = 0.7')

kernel_pca(np.copy(numm),0.8,'Radial basis sigma = 0.8')

kernel_pca(np.copy(numm),0.9,'Radial basis sigma = 0.9')

kernel_pca(np.copy(numm),1,'Radial basis sigma = 1')