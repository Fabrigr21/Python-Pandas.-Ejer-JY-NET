#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


datos = {'A': [1, 2, 3, 4, 5], 'B': [9, 8, 7, 6, 5], 'C': [2, 3, 5, 7, 11]} 
        
df = pd.DataFrame(data=datos)

df


# In[5]:


type(df)


# In[11]:


columna = df.ix[:,1]

columna


# In[12]:


type(columna)


# In[ ]:




