#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[6]:


# Importing data
data=pd.read_csv('owid-monkeypox-data.csv')


# In[7]:


data.head(10)


# In[8]:


data.info()


# In[9]:


#Checking for null values
data.isnull().sum()


# In[10]:


#Substituting null values with zero
data.fillna(0)


# In[11]:


#Confirming the countries included in location
countries=data.location.unique()
countries


# In[12]:


# Deleting 'World' From Location to avoid replication. 'World' is believed to be a combination of all the countries('Location) 
data=data[data['location']!='World'].copy()
country=data.location.unique()
country


# In[13]:


#Confirming the number of Countires in the data
len(country)


# In[14]:


#To determine the total cases of monkeypox per country, new cases were grouped and sum by each location 
Total_case_per_Country = data.set_index('location').groupby(level=0)['new_cases'].agg(np.sum).sort_values(ascending=False)
Total_case_per_Country.head(10)


# In[15]:


#To determine the total deaths of monkeypox per country, new deaths were grouped and sum by each location 
Total_deaths_per_Country = data.set_index('location').groupby(level=0)['new_deaths'].agg(np.sum).sort_values(ascending=False)
Total_deaths_per_Country.head(10)


# In[16]:


from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

print(__version__) # requires version >= 1.9.0


# In[17]:


import cufflinks as cf


# In[18]:


cf.go_offline()


# In[19]:


#Visualizing the 10 top deaths 
Total_deaths_per_Country.head(10).iplot(kind='bar',xTitle='location',title='Top 10-Total Death per Location')


# In[20]:


#Visualizing the 10 top cases 
Total_case_per_Country.head(10).iplot(kind='bar',xTitle='location',title='Top 10 -Total Cases per Location')


# In[21]:



data[data['location'] == 'United States']


# In[22]:


#Visualizing the spread in location with the highest number of cases (United States)
sns.relplot(data=data[data['location'] == 'United States'], kind="line", x="date", y="new_cases")


# In[23]:


data[data['location'] =='Nigeria']


# In[117]:


#Visualizing the spread in location with the highest number of death (Nigeria)
sns.relplot(data=data[data['location'] =='Nigeria'], kind="line", x="date", y="new_cases")













