#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


datos = ['1.1', 'Python', '0.5', 'pandas', '2.8']

serie = pd.Series(datos)

serie


# In[5]:


serie = pd.Series(serie).sort_values()


# In[6]:


serie


# In[ ]:




