#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


bookings = pd.read_csv('hotel_booking_data.csv', parse_dates = True)


# In[3]:


bookings


# In[4]:


bookings.info()


# In[5]:


bookings.head()


# In[6]:


city = bookings[bookings["hotel"] == "City Hotel"]
resort = bookings[bookings["hotel"] == "Resort Hotel"]


# In[11]:


city.head()


# In[12]:


resort.head()


# In[16]:


bookings['total_stay'] = bookings['stays_in_week_nights']+bookings['stays_in_weekend_nights']


# In[17]:


# Total number of guests
bookings['guests'] = bookings['adults']+bookings['children'] +bookings['babies']


# In[19]:


bookings = bookings[bookings.deposit_type=="No Deposit"]
bookings.groupby(['deposit_type','is_canceled']).count()


# In[21]:


bookings["lead_time"].max()


# In[23]:


bookings.shape


# In[24]:


bookings.dropna()


# In[25]:


bookings.drop("lead_time",axis=1)


# In[ ]:




