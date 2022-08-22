#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?
# 

# In[ ]:


def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("enter your no."))
for i in range(n):
    print(fibo(i))
    


# 2. Write a Python Program to Find Factorial of Number Using Recursion?
# 

# In[ ]:


def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
n=int(input("enter your no."))    
print(fact(n))


# 3. Write a Python Program to calculate your Body Mass Index?
# 

# In[ ]:


def bmi_calculator(height,weight):
    BMI = weight / (height/100)**2
    print(BMI)
    
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

bmi_calculator(height,weight)


# 4. Write a Python Program to calculate the natural logarithm of any number?
# 

# In[ ]:


import math
n=float(input("enter your no."))
print("the natural log of {} is {}".format(n,math.log(n)))


# 5. Write a Python Program for cube sum of first n natural numbers?

# In[ ]:


def cubesum(n):
    for i in range(1,n+1):
        d=d+i**3
        
    return d
n=int(input("enter your no."))
print(cubesum(n))


# In[ ]:




