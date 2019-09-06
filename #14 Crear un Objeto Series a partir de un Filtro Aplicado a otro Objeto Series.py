#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


datos = [0, 1, 2, 3, 4, 5 ,6 ,7 , 8, 9]

serie = pd.Series(datos)

serie


# In[3]:


n = 6

serie_nueva = serie[serie < n]

serie_nueva


# In[ ]:




