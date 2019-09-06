#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


datos = pd.Series(['100', '200', 'python', '300.15', '500.8'])

datos


# In[3]:


datos = pd.to_numeric(datos, errors='coerce')

datos


# In[ ]:




