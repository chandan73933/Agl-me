#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inLine')


# In[2]:


df =pd.read_csv("Desktop/311804509.csv")


# In[3]:


df.head(5)


# In[4]:


df.shape


# In[5]:


df.count()


# In[6]:


df_c=df.head(20).loc[df['call_type']=='General Info']


# In[7]:


df_d=df.head(10).loc[df['call_type']=='Technical Query']


# In[8]:


df.columns


# In[9]:


df.info()


# In[10]:


df.describe()


# In[11]:


df.isnull()


# In[12]:


df.dtypes


# In[13]:


df.city.value_counts()


# In[14]:


df_e=df.head(15).loc[df['call_type']=='Installation']


# In[15]:


df.groupby(['city','state_new','zipcode']).size().reset_index()#.head()


# In[16]:


df.iloc[:5,:2]


# In[17]:


x=df.iloc[0:10,13:16]


# In[18]:


x.head(20)


# In[19]:


#plt.plot(df_c['is_it_under_warranty'],np.zeros_like(df_c['is_it_under_warranty']),'o')
#plt.plot(df_d['is_it_under_warranty'],np.zeros_like(df_d['is_it_under_warranty']),'o')
#plt.plot(df_e['model_codes'],np.zeros_like(df_e['model_codes']),'o')
#plt.show()


# In[20]:


df.iloc[0:6,:1]


# In[21]:


df.iloc[0:6,28:29]


# In[22]:


df.groupby(['cdp_customer_id','state_new','model','call_type','service_details_dealer_name','industry_std_desc','mg4_des',]).size().reset_index().head(60)


# In[23]:


final=df.groupby(['cdp_customer_id','state_new','model','call_type','service_details_dealer_name','industry_std_desc','mg4_des',]).size().reset_index().head(80)
df_c=final.loc[df['mg4_des']=='Android']
df_e=final.loc[df['mg4_des']=='Linux']
df_f=final.loc[df['mg4_des']=='Inactive']
plt.plot(df_c['cdp_customer_id'],np.zeros_like(df_c['cdp_customer_id']),'o')
plt.plot(df_e['cdp_customer_id'],np.zeros_like(df_e['cdp_customer_id']),'o')
plt.plot(df_f['cdp_customer_id'],np.zeros_like(df_f['cdp_customer_id']),'o')
plt.xlabel('customer_id')
plt.ylabel('os')
plt.show()


# In[24]:


sns.FacetGrid(final,hue="mg4_des",size=10).map(plt.scatter,"model","service_details_dealer_name").add_legend();
plt.show()


# In[25]:


sns.FacetGrid(final,hue="mg4_des",size=7).map(plt.scatter,"industry_std_desc","state_new").add_legend();
plt.show()


# In[26]:


sns.FacetGrid(final,hue="mg4_des",size=11).map(plt.scatter,"call_type","state_new").add_legend();
plt.show()


# In[ ]:





# In[32]:


sns.pairplot(final,hue='cdp_customer_id',size=3)
plt.show()


# In[ ]:





# In[ ]:




