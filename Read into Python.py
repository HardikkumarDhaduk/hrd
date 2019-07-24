#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
from sklearn.feature_extraction.text import CountVectorizer


# In[2]:


data = pd.read_csv('google_play_store_apps_reviews_training.csv')

