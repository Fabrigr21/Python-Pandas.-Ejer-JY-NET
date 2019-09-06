#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[4]:


datos = [['Colombia', 'Perú', 'Bolivia', 'Argentina'], ['Bolivia', 'Uruguay'], ['Chile']]

serie = pd.Series(datos)

serie


# In[7]:


serie = serie.apply(pd.Series).stack().reset_index(drop=True)

serie


# In[9]:


type(serie)


# In[ ]:




