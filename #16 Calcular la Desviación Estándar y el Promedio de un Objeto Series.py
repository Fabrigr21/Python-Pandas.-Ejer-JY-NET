#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


datos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

serie = pd.Series(datos)

serie


# In[7]:


serie.std()    #desviacion estandar


# In[8]:


serie.mean()    #promedio


# In[ ]:




