#!/usr/bin/env python
# coding: utf-8

# # Name: Monika Choudhary
# 
# ## Company name : Codtech IT Solutions
# 
# ## Id :CT8DS1233
# 
# ## Domain: Data Science
# 
# ## Duration : 2 months
# 
# ## Project : Exploratory data analysis on Superstore Dataset

# In[2]:


import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np


# In[13]:


dataset = pd.read_excel('C:\\Users\\monica\\Downloads\\superstore\\superstore.xlsx')


# In[14]:


dataset.head()


# In[15]:


dataset.shape #checking rows and columns 


# In[16]:


dataset.isnull().sum() # checking missing values


# In[17]:


dataset['Ship Mode'].value_counts()


# In[20]:


sns.countplot(x='Ship Mode',data=dataset)
plt.title("Count of Ship Mode")
plt.savefig("count of ship mode.jpg")
plt.show()


# In[21]:


dataset['Region'].value_counts()


# In[29]:


x = dataset['Region'].value_counts().index
print(x)
y = dataset['Region'].value_counts().values
print(y)


# In[45]:


plt.pie(y,labels=x,startangle = 90,autopct="%0.2f%%")
plt.legend()
plt.show()


# In[46]:


sns.countplot(x='Ship Mode',data=dataset,hue='Category')
plt.show()


# In[47]:


sns.countplot(x='Segment',data=dataset)
plt.title("Count of Segment")
#plt.savefig("count of ship mode.jpg")
plt.show()


# In[48]:


sns.countplot(x='Category',data=dataset)
plt.title("Count of Category")

plt.show()


# In[61]:


plt.figure(figsize=(5,6))
sns.countplot(x='Category',data=dataset[dataset['Category']=='Furniture'],hue='Sub-Category')
plt.show()


# In[62]:


dataset["Order Year"] = dataset['Order Date'].dt.year


# In[63]:


dataset.info()


# In[64]:


dataset['Order Year'].value_counts()


# In[65]:


sns.countplot(x='Order Year',data=dataset)
plt.title("Count ofOrder Year")

plt.show()


# In[68]:


sns.barplot(x='Category',y="Profit",data=dataset,estimator='sum')
plt.show()


# In[70]:


dataset['City'].value_counts()[:5]


# In[71]:


dataset.info()


# In[72]:


sns.barplot(x='Category',y="Quantity",data=dataset,estimator='sum')
plt.show()


# In[ ]:




