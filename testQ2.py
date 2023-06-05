#!/usr/bin/env python
# coding: utf-8

# In[5]:


def first_unique_char(string):
    seen = set()
    for i, char in enumerate(string):
        if char not in seen:
            return i
        seen.add(char)
    return -1


string = "aabbss"
print(first_unique_char(string))


# In[ ]:




