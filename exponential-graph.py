#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyplot from matplotlib


# In[ ]:





# In[2]:


import matplotlib.pyplot as plt


# In[3]:


plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()


# In[6]:


import numpy as np


# In[7]:


t = np.arange(0., 5., 0.2)


# In[8]:


import math


# In[9]:


y = math.exp(1)


# In[10]:


print(y)


# In[11]:


plt.plot(t, math.exp(t), 'r--')


# In[12]:


z = math.exp(t)


# In[13]:


def f(x):
    return math.exp(x)

    


# In[15]:


z = np.vectorize(f)


# In[18]:


plt.plot(t, z(t), 'r--')


# In[ ]:




