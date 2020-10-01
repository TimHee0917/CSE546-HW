#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
A = ([0,2,4],
     [2,4,2],
     [3,3,1]);
b = ([-2],[-2],[-4]);
c = ([1],[1],[1]);
A_inv = np.linalg.inv(A)
print(A_inv)
print(A_inv.dot(b))
print(np.dot(A,c))


# In[ ]:





# In[ ]:





# In[ ]:




