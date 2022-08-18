#!/usr/bin/env python
# coding: utf-8

# 1. Is the Python Standard Library included with PyInputPlus?

# In[ ]:


No, the Python Standard Library not included with PyInputPlus so we have install it separately using Pip


# 2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?

# In[ ]:


We commonly import pyinputplus as pypi so that we can enter a shorter name when calling the module's functions 


# 3. How do you distinguish between inputInt() and inputFloat()?

# In[ ]:


The inputInt() function returns an integer, while the inputFloat() function returns a float value.


# 4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?

# In[ ]:


By using pyip.inputint(min=0, max=99)


# 5. What is transferred to the keyword arguments allowRegexes and blockRegexes?

# In[ ]:


A list of regex strings that are either explicitly allowed or denied


# 6. If a blank input is entered three times, what does inputStr(limit=3) do?

# In[ ]:


The function will raise RetryLimitException.


# 7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?

# In[ ]:


The function returns the value 'hello'

