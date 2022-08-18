#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Write a Python program to convert kilometers to miles');get_ipython().run_line_magic('pinfo', 'miles')


# In[ ]:


mile_con=0.621371 #conversion factor
km=float(input("enter your kilometer"))
miles=km*mile_con #converting kilometer to miles
print("miles:",miles)


# In[ ]:


get_ipython().set_next_input('2. Write a Python program to convert Celsius to Fahrenheit');get_ipython().run_line_magic('pinfo', 'Fahrenheit')


# In[ ]:


#converting celsius to fahrenheit
celsius=38 
fahrenheit = (celsius * 1.8) + 32


# In[ ]:


get_ipython().set_next_input('3. Write a Python program to display calendar');get_ipython().run_line_magic('pinfo', 'calendar')


# In[ ]:


import calendar
year=int(input("enter your year"))
mon=int(input("enter your month"))
print(calendar.month(year,mon))


# In[ ]:


get_ipython().set_next_input('4. Write a Python program to solve quadratic equation');get_ipython().run_line_magic('pinfo', 'equation')


# In[ ]:


import cmath
a=10
b=16
c=5
d=(b**2-4*a*c)
root1=(-b+cmath.sqrt(d))/(2*a)
root2=(-b-cmath.sqrt(d))/(2*a)
print("the root are {} and {}".format(root1,root2))


# In[ ]:


get_ipython().set_next_input('5. Write a Python program to swap two variables without temp variable');get_ipython().run_line_magic('pinfo', 'variable')


# In[ ]:


x = 89
y = 45
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
 
x, y = y, x
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)

