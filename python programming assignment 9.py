#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to check if the given number is a Disarium Number?

# In[8]:


def disarium(n):
    n=str(n)
    d,l=1,0
    for i in n:
        l=l+int(i)**d
        d+=1
    return l

n=int(input("enter your no."))
if n==disarium(n):
    print("yes it is disarium")
else:
    print("no it is not disarium")
        
        


# 2. Write a Python program to print all disarium numbers between 1 to 100?

# In[11]:


def disarium(n):
    n=str(n)
    d,l=1,0
    for i in n:
        l=l+int(i)**d
        d+=1
    return l
for i in range(1,100):
    if i==disarium(i):
        print(i)


# 3. Write a Python program to check if the given number is Happy Number?

# In[19]:


def happy(n):
    n=str(n)
    if len(n)==1:
        if n=="1":
            return "happy no." 
        else:
             return ("not happy no.")
    else:
        d=0
        for i in n:
            d=d+int(i)**2
        return happy(d)  
    
n=35
print(happy(n))
            


# 4. Write a Python program to print all happy numbers between 1 and 100?

# In[20]:


def happy(n):
    n=str(n)
    if len(n)==1:
        if n=="1":
            return True
        else:
             return False
    else:
        d=0
        for i in n:
            d=d+int(i)**2
        return happy(d)  
    
for i in range(1,100):
    if happy(i)== True:
        print(i)


# 5. Write a Python program to determine whether the given number is a Harshad Number?

# In[25]:


def harshad(n):
    d=0
    for i in str(n):
        d=d+int(i)
    if int(n)%d==0:
        return ("harshad no.")
    else:
        return ("not harshad no.")
n=int(input("enter your no."))
print(harshad(n))


# 6. Write a Python program to print all pronic numbers between 1 and 100?

# In[31]:


import math
def pronic(n):
    d=int(math.sqrt(n))+1
    for i in range(1,d):
        if i*(i+1)==n:
            return True
n=int(input())
if pronic(n)==True:
    print("yes it is pronic")
else:
    print("no it is not pronic")
        


# In[ ]:





# In[29]:





# In[ ]:




