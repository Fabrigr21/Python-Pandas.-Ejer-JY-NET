#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


datos = ['Python', 'C#', 'C++', 'Java', 'PHP']

serie = pd.Series(datos)

serie


# In[3]:


serie = serie.append(pd.Series(['JavaScript', 'Perl']))

serie


# In[ ]:




