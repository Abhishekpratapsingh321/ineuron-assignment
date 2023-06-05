#!/usr/bin/env python
# coding: utf-8

# In[1]:


def movezero(arr):
    l=0
    for r in range(len(arr)):
        if(arr[r]!=0):
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
    return arr
arr=[0,3,2,1,0,5,0,0,3,4]
print(movezero(arr))


# In[ ]:




