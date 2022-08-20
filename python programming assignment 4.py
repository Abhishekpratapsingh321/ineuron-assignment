#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to Find the Factorial of a Number?

# In[ ]:


#program to find factorial of a no.
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
#taking input from user    
n=int(input()) 
print(factorial(n))


# In[ ]:


get_ipython().set_next_input('2. Write a Python Program to Display the multiplication Table');get_ipython().run_line_magic('pinfo', 'Table')


# In[ ]:


#print table
def table(n):
    for i in range(1,11):
        print("{} * {} = {}".format(n,i,n*i))
# takin input from user        
n=int(input())
table(n)


# In[ ]:


get_ipython().set_next_input('3. Write a Python Program to Print the Fibonacci sequence');get_ipython().run_line_magic('pinfo', 'sequence')


# In[ ]:


def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+ fibo(n-2)
    
n=int(input())    
for i in range(n):
    print(fibo(i))


# In[ ]:


get_ipython().set_next_input('4. Write a Python Program to Check Armstrong Number');get_ipython().run_line_magic('pinfo', 'Number')


# In[ ]:


def armstrong(n):
    x,d=0,0
    while n>0:
        d=n%10
        x=x+d**3
        n=n//10
    else:
        return x
n=int(input())
if n==int(armstrong(n)):
     print("yes armstrong")
else:
     print("not armstrong")
        


# In[ ]:


get_ipython().set_next_input('5. Write a Python Program to Find Armstrong Number in an Interval');get_ipython().run_line_magic('pinfo', 'Interval')


# In[ ]:


def armstrong(n):
    x,d=0,0
    while n>0:
        d=n%10
        x=x+d**3
        n=n//10
    else:
        return x
    
n=int(input())
for i in range(1,n+1):
    if i==int(armstrong(i)):
        print(i)


# In[ ]:


get_ipython().set_next_input('6. Write a Python Program to Find the Sum of Natural Numbers');get_ipython().run_line_magic('pinfo', 'Numbers')


# In[ ]:


def sum(n):
    d=0
    for i in range(1,n+1):
        d=d+i
    else:
        return d
n=int(input())
print(sum(n))
        


# In[ ]:




