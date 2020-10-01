#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
n = 40000
Z=np.random.randn(n);
import matplotlib.pyplot as plt
plt.step(sorted(Z), np.arange(1,n+1)/float(n)) 
plt.xlim(-3,3)
plt.xlabel("x")
plt.ylabel("F_hat")

Y_1 = np.sum(np.sign(np.random.randn(n, 1))*np.sqrt(1./1), axis=1)
Y_8 = np.sum(np.sign(np.random.randn(n, 8))*np.sqrt(1./8), axis=1)
Y_64 = np.sum(np.sign(np.random.randn(n, 64))*np.sqrt(1./64), axis=1)
Y_512 = np.sum(np.sign(np.random.randn(n, 512))*np.sqrt(1./512), axis=1)
plt.step(sorted(Y_1), np.arange(1,n+1)/float(n))
plt.step(sorted(Y_8), np.arange(1,n+1)/float(n))
plt.step(sorted(Y_64), np.arange(1,n+1)/float(n))
plt.step(sorted(Y_512), np.arange(1,n+1)/float(n))
plt.legend(["Gaussian","1","8","64","512"],loc="upper right")


# In[ ]:




