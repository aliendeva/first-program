#!/usr/bin/env python
# coding: utf-8

# In[2]:


dd = 22
mm = 2
yyyy =2022

mm1 = [1,3,5,7,8,10,12]
mm2 = [2]
mm3 = [4,6,9,11]


# In[3]:


date = (f"{dd}/{mm}/{yyyy}")


# In[4]:


a = mm in mm1 and dd <= 31 and (dd or mm != 0)
b = mm in mm2 and dd <= 28 and (dd or mm != 0)
b1 = mm in mm2 and (yyyy % 4 == 0) and dd <= 29 and dd != 0
c = mm in mm3 and dd <= 30 and (dd or mm != 0)
if a or b or b1 or c == True:
    print(date)
    
else: print("invalid date")


# In[ ]:





# In[ ]:




