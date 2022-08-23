#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to find sum of array?

# In[1]:


def _sum(n):
    d=0
    for i in n:
        d=d+i
    return d

n=[2,3,4,5,6,7,8]
print(_sum(n))


# 2. Write a Python Program to find largest element in an array?

# In[3]:


def largest(n):
    n.sort()
    return n[len(n)-1]
n=[2,3,4,5,6,7,8,5,4,23,11,12]
print(largest(n))


# 3. Write a Python Program for array rotation?

# In[6]:


try:
    def left_rotate(n,d):
        n[:]=n[d:len(n)]+n[0:d]
        return n

    n=list(map(int,input().split()))
    d=int(input("enter till how much you have to return"))
    print("after rotation:",rotate(n,d))
    
except exception as e:
    print(e)


# 4. Write a Python Program to Split the array and add the first part to the end?

# In[ ]:


try:
    def _split(n,d):
        n[:]=n[d:len(n)]+n[0:d]
        return n

    n=list(map(int,input().split()))
    d=int(input("enter till how much index you have to split"))
    print("after spilting",_split(n,d))
    
except exception as e:
    print(e)


# 5. Write a Python Program to check if given array is Monotonic?

# In[8]:


def isMonotonic(A):
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
  
# Driver program

A=list(map(int,input().split()))  
# Print required result
print(isMonotonic(A))


# In[ ]:




