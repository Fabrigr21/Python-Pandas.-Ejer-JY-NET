#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


datos = [1, 2, 3, 4, 5]

indices = ['A', 'B', 'C', 'D', 'E']

serie = pd.Series(data=datos, index=indices)

serie


# In[4]:


serie = serie.reindex(index=['B', 'A', 'C', 'D', 'E'])

serie


# In[ ]:




