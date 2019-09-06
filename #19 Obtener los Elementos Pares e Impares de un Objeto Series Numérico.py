#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


datos = list(range(10))

datos


# In[4]:


serie = pd.Series(datos)

serie


# In[5]:


pares = serie[serie %2 == 0]

pares


# In[6]:


impares = serie[serie %2 == 1]

impares


# In[ ]:




