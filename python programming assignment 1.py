#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to print 'Hello Python'

# In[ ]:


print("Hello Python") #printing hello python


# 2. Write a Python program to do arithmetical operations addition and division.?

# In[ ]:


x,y=10,2 #initializing the value of x and y
add=x+y #addition opeartion
div=x/y #division operation
print("addition of x and y",add)
print("division of x and y",div)


# 3. Write a Python program to find the area of a triangle?

# In[ ]:


# Three sides of the triangle is a, b and c:
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
# calculate the semi-perimeter.
s = (a + b + c) / 2.
# calculate the area.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5.


# 4. Write a Python program to swap two variables?

# In[ ]:


x,y=5,4
#swapping x and y
x,y=y,x


# 5. Write a Python program to generate a random number?

# In[ ]:


import random 
n=random.random()
print(n)


# In[ ]:




