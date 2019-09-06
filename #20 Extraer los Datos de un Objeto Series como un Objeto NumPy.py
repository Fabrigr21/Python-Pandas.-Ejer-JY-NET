#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


datos = list(range(10))

datos


# In[3]:


serie = pd.Series(datos)

serie


# In[4]:


type(serie)


# In[5]:


arreglo = serie.values

arreglo


# In[6]:


type(arreglo)


# In[ ]:




