#!/usr/bin/env python
# coding: utf-8

# In[1]:


Players = ['Kohli','dhoni','yuvi','sachin','vijaShankar']
print(Players[2:3])


# In[5]:


li=[2,3,1,6,8,10,3]

print(li[:])


# In[3]:


print(li[2:3])


# In[6]:


print(li[2:4])


# In[7]:


li_cp=li[:]
print(li_cp)


# In[10]:


li_cp.append(100)


# In[11]:


print(li_cp)


# In[13]:


li_cp.pop()


# In[14]:


print(li_cp)


# In[24]:


for s in li_cp[:5]:
    print(li_cp[s])


# In[ ]:




