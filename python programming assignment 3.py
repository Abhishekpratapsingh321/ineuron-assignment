#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input("enter your no."))


# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
# 

# In[ ]:


#to find no. is positive, negative, or zero
if n>0: # for positive
    print("positive")
elif n<0: # for negative
    print("negative")  
else:
    print("zero")


# 2. Write a Python Program to Check if a Number is Odd or Even?
# 

# In[ ]:


# to find no. is odd or even
#  no divided by 2 is even otherwise odd
if n%2==0:
    print("Even")
else:
    print("Odd")


# In[ ]:


get_ipython().set_next_input('3. Write a Python Program to Check Leap Year');get_ipython().run_line_magic('pinfo', 'Year')


# In[ ]:


# to check for leap year
# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (n % 400 == 0) and (n % 100 == 0):
    print("{0} is a leap year".format(n))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (n % 4 ==0) and (n % 100 != 0):
    print("{0} is a leap year".format(n))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(n))


# In[ ]:


get_ipython().set_next_input('4. Write a Python Program to Check Prime Number');get_ipython().run_line_magic('pinfo', 'Number')


# In[ ]:


import math

if n==1:
    print("no. is not prime")
elif n==2:
    print("no. is prime")
elif n%2==0:
    print("no. is not prime")
else:
    d=0
    x=math.floor(math.sqrt(n))
    for i in range(3,x+1,2):
        if n%i==0:
            d=d+1
            break
    if d==0:
        print("no. is prime")
    else:
        print("no. is not prime")


# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[ ]:


import math
def prime(n):
    if n==1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
       
        x=math.floor(math.sqrt(n))
        for i in range(3,x+1,2):
            if n%i==0:
                return False
        return True
            
for  i in range(1,10001):
    if prime(i)==True:
        print(i)


# In[ ]:




