#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to find sum of elements in list?

# In[ ]:


l=list(map(int,input().split()))
print(sum(l))


# 2. Write a Python program to Multiply all numbers in the list?

# In[5]:


import functools
import operator
l=list(map(int,input().split()))
print(functools.reduce(operator.mul,l))
    


# 3. Write a Python program to find smallest number in a list?

# In[8]:


l=list(map(int,input().split()))
l.sort()
l[0]


# 4. Write a Python program to find largest number in a list?

# In[10]:


l=list(map(int,input().split()))
l[-1]


# 5. Write a Python program to find second largest number in a list?

# In[13]:


l=list(map(int,input().split()))
a=list(set(l))
print(a[-2])


# 6. Write a Python program to find N largest elements from a list?

# In[20]:


l=list(map(int,input().split()))
n=int(input("enter the value of N"))
l=list(set(l))
l.sort()
print(l[len(l)-(n):len(l)])


# 7. Write a Python program to print even numbers in a list?

# In[21]:


l=list(map(int,input().split()))
l=[i for i in l if i%2==0]
print(l)


# 8. Write a Python program to print odd numbers in a List?

# In[ ]:


l=list(map(int,input().split()))
l=[i for i in l if i%2!=0]
print(l)


# 9. Write a Python program to Remove empty List from List?

# In[32]:


l=[[1,4,6],[4,7],[],[8],8,9,9]
l=[i for i in l if i!=[]]
l


# 10. Write a Python program to Cloning or Copying a list?

# In[34]:


#through assignment operator
def clone(l):
    l2=l
    return l2
l=list(map(int,input().split()))
l2=clone(l)
l2


# 11. Write a Python program to Count occurrences of an element in a list?

# In[37]:


l=list(map(int,input().split()))
n=int(input("enter the element whose occurence you have to check"))
s=list(set(l))
d=l.count(n)
print("the occurence of {} is {}".format(n,d))


# In[ ]:





# In[ ]:




