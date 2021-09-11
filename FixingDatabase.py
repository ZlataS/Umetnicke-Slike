#!/usr/bin/env python
# coding: utf-8

# In[30]:


import torch
import torchvision
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import shutil
from geomloss import SamplesLoss


# In[2]:


info_path = 'C:\\Users\\zlata\\Downloads\\paintings\\imagesinfo.csv' 
info = pd.read_csv('C:\\Users\\zlata\\Downloads\\paintings\\imagesinfo.csv') #nazivi slika i kategorije
images_path = 'C:\\Users\\zlata\\Downloads\\paintings\\images'


# In[6]:


TOP_N = 3
top_genres = info['genre'].value_counts()[0:TOP_N].reset_index()
top_genres.columns = ['genre', 'count']
top_genres['class_weight'] = top_genres['count'].sum() / (top_genres.shape[0] * top_genres['count'])
top_genres


# In[7]:


TOP_N = 2
top_genres = info['genre'].value_counts()[0:TOP_N].reset_index()
top_genres.columns = ['genre', 'count']
top_genres['class_weight'] = top_genres['count'].sum() / (top_genres.shape[0] * top_genres['count'])
top_genres


# In[8]:


filter_list = top_genres['genre']
filter_list = filter_list.tolist()
filter_list


# In[11]:


fdata = info[info['genre'].isin(filter_list)]
images = fdata[['filename','genre']]
images.reset_index(drop= True, inplace=True)
images["filename"] = 'C:\\Users\\zlata\\Downloads\\paintings\\images\\'+images["filename"]

artgenres = fdata['genre'].unique()
artgenres


# In[13]:


fdata.to_csv('filtered.csv')
portrait = images[images["genre"] == "portrait"]
portrait.reset_index(drop= True, inplace=True) 
portrait = portrait['filename'].values.tolist()


# In[14]:


landscape = images[images["genre"] == "landscape"]
landscape.reset_index(drop= True, inplace=True) 
landscape = landscape['filename'].values.tolist()


# In[16]:


import os


# In[17]:


mypath = "C:\\Users\\zlata\\Downloads\\paintings\\images" 
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]


# In[19]:


portrait_folder = os.path.join("./", "portrait")
landscape_folder = os.path.join("./", "landscape")


# In[20]:


if not os.path.exists(portrait_folder): os.makedirs(portrait_folder)
if not os.path.exists(landscape_folder): os.makedirs(landscape_folder)


# In[23]:


for i in portrait:
    shutil.copy(i, portrait_folder)
for i in landscape:
    shutil.copy(i, landscape_folder)


# In[24]:


fil_info = pd.read_csv('C:\\Users\\zlata\\filtered.csv')
fil_info.head()


# In[26]:


filtered_imgdir = "C:\\Users\\zlata\\images"


# In[28]:


get_ipython().system('pip3 install geomloss')


# In[31]:


portraits_path = "C:\\Users\\zlata\\images\\portrait"
landscapes_path = "C:\\Users\\zlata\\images\\landscape"


# In[56]:


top_genres = info['genre'].value_counts()[0:1].reset_index()
top_genres.columns = ['genre', 'count']
top_genres['class_weight'] = top_genres['count'].sum() / (top_genres.shape[0] * top_genres['count'])
top_genres

filter_list = top_genres['genre']
filter_list = filter_list.tolist()
filter_list

fdataportrait = fil_info[fil_info['genre'].isin(filter_list)]
fdataportrait.to_csv('filteredportrait.csv')
fil_info_portrait = pd.read_csv('C:\\Users\\zlata\\filteredportrait.csv')
fil_info_portrait.head()


# In[46]:


n = fil_info['filename'].values
print(n)


# In[60]:


n = fil_info_portrait['filename'].values
fig, axes = plt.subplots(1, 5, figsize=(20,10))
j = 0
for i in n:
    #random_art = random.choice(fil_info['filename'].values)
    image_file = 'C:/Users/zlata/images/portrait/'+ i
    image = plt.imread(image_file)
    axes[j].imshow(image)
    #axes[j].set_title("Art: " + random_art.replace('_', ' '))
    axes[j].axis('off')
    j=j+1
print(random_image_file)
plt.show()


# In[61]:


top_genres = info['genre'].value_counts()[1:2].reset_index()
top_genres.columns = ['genre', 'count']
top_genres['class_weight'] = top_genres['count'].sum() / (top_genres.shape[0] * top_genres['count'])
top_genres

filter_list = top_genres['genre']
filter_list = filter_list.tolist()
filter_list

fdatalandscape = fil_info[fil_info['genre'].isin(filter_list)]
fdatalandscape.to_csv('filteredlandscape.csv')
fil_info_landscape = pd.read_csv('C:\\Users\\zlata\\filteredlandscape.csv')
fil_info_landscape.head()


# In[63]:


n = fil_info_landscape['filename'].values
fig, axes = plt.subplots(1, 5, figsize=(20,10))
j = 0
for i in n:
    #random_art = random.choice(fil_info['filename'].values)
    image_file = 'C:/Users/zlata/images/landscape/'+ i
    image = plt.imread(image_file)
    axes[j].imshow(image)
    #axes[j].set_title("Art: " + random_art.replace('_', ' '))
    axes[j].axis('off')
    j=j+1
print(random_image_file)
plt.show()


# In[ ]:




