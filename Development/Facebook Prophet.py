#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Using Git Bash install the following in order
# 1. conda install -c anaconda ephem
# 2. conda install -c conda-forge pystan
# 3. conda install -c conda-forge fbprophet


# In[1]:


from fbprophet import Prophet
import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt


# In[2]:


dataset = pd.read_csv('IPG2211A2N.csv')
dataset.head()


# In[3]:


dataset.dtypes


# In[4]:


dataset['DATE'] = pd.to_datetime(dataset.DATE)
dataset.dtypes


# In[5]:


dataset = dataset.rename(columns = {"DATE" : 'ds', "IPG2211A2N" : 'y'})
dataset.head()


# In[6]:


model = Prophet()
model.add_country_holidays(country_name='CA')
model.fit(dataset)
future = model.make_future_dataframe(periods = 42)


# In[7]:


forecast = model.predict(future)


# In[8]:


forecast


# In[9]:


model.plot_components(forecast)


# In[10]:


dataset.tail(10)


# In[11]:


future.tail()


# In[12]:


forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()


# In[13]:


plot = model.plot(forecast)


# In[14]:


forecast.to_csv('output.csv')


# In[ ]:




