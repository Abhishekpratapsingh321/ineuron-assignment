#!/usr/bin/env python
# coding: utf-8

# Question 1:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated
# sequence.

# In[6]:


import math
D=input()
C,H=50,30
D=D.split(",")
q=[round(math.sqrt((2 * C * int(i))/H)) for i in D]
print(q)


# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
# element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡Y-1.

# In[15]:


x=int(input())
y=int(input())
a=[[i*j for i in range(y)] for j in range(x)]
print(a)


# Write a program that accepts a comma separated sequence of words as input and prints the
# words in a comma-separated sequence after sorting them alphabetically.

# In[17]:


words=input().split(",")
words=sorted(words)
print(words)


# Write a program that accepts a sequence of whitespace separated words as input and prints
# the words after removing all duplicate words and sorting them alphanumerically.

# In[19]:


words=input().split(" ")
words=sorted(set(words))
print(words)


# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:

# In[26]:


a=input()
c,d=0,0
for i in a:
    if i.isalpha():
        c=c+1
    elif i.isdigit():
        d=d+1
print(c,d)    
        


# A website requires the users to input username and password to register. Write a program to
# check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them
# according to the above criteria. Passwords that match the criteria are to be printed, each
# separated by a comma.

# In[27]:


import re

passwords = input("Type in: ").split(",")


accepted_pass = []
for i in passwords:
    
    if len(i) < 6 or len(i) > 12:
        continue

    elif not re.search("([a-z])+", i):
        continue

    elif not re.search("([A-Z])+", i):
        continue

    elif not re.search("([0-9])+", i):
        continue

    elif not re.search("([!@$%^&])+", i):
        continue

    else:
        accepted_pass.append(i)

print((" ").join(accepted_pass))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




