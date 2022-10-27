#!/usr/bin/env python
# coding: utf-8

# In[1]:



import findspark
findspark.init()
findspark.find()


# In[2]:


#import pyspark
from pyspark.sql import SparkSession


# In[3]:


#create SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()


# In[4]:


#data
data=[("Java","20000"),("python","100000"),("scala","3000")]
#columns
columns=["language","user_count"]


# In[5]:


#create dataframe

df=spark.createDataFrame(data).toDF(*columns)


# In[6]:


#print dataframe
df.show()


# In[ ]:




