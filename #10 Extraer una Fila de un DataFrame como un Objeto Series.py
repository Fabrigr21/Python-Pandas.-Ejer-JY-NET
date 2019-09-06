#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[3]:


datos = {'A': [1, 2, 3, 4, 5], 'B':[6, 5, 4, 3, 2], 'C':[2, 3, 5, 7, 11]}

df = pd.DataFrame(data=datos)
         
df 


# In[4]:


fila =df.iloc[2,:]

fila


# In[5]:


type(fila)


# In[ ]:




