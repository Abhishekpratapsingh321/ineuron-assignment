#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to find words which are greater than given length k?

# In[1]:


def greater(string,k):
    l=list(map(str,string.split()))
    l=[i for i in l if len(i)>k]
    return l
string=input("enter your string")
k=int(input("enter your length"))
print(greater(string,k))


# 2. Write a Python program for removing i-th character from a string?

# In[10]:


def a_remove(string,i):
    string=string[0:i]+string[i+1:(len(string))]
    return string
string=input("enter your string")
i=int(input("enter your ith character"))
print(a_remove(string,i-1))      


# 3. Write a Python program to split and join a string?

# In[15]:


def split_string(string):
 
    # Split the string based on space delimiter
    list_string = string.split(' ')
     
    return list_string
 
def join_string(list_string):
 
    # Join the string based on '-' delimiter
    string = '-'.join(list_string)
     
    return string
 
# Driver Function
if __name__ == '__main__':
    string = input("enter your string")
     
    # Splitting a string
    list_string = split_string(string)
    print(list_string)
 
     # Join list of strings into one
    new_string = join_string(list_string)
    print(new_string)


# 4. Write a Python to check if a given string is binary string or not?

# In[36]:


def check(string):
    a=set(string)
    if a=={"1","0"} or a=={'0'} or a=={'1'}:
        print("yes binary")
    else: 
        print("not binary")
string=input("enter your string")
check(string)


# 5. Write a Python program to find uncommon words from two Strings?

# In[47]:


def uncommon(string1,string2):
    lst_unco=[i for i in "".join(string2).split() if i not in "".join(string1).split()]
    lst_2unco=[i for i in "".join(string1).split() if i not in "".join(string2).split()]
    return lst_unco+lst_2unco

string1=input("enter your 1st string")
string2=input("enter your 2nd string")
print(uncommon(string1,string2))


# In[ ]:


get_ipython().set_next_input('6. Write a Python to find all duplicate characters in string');get_ipython().run_line_magic('pinfo', 'string')


# In[65]:


def duplicate(string):
    l=string.split()
    a=set(string.split())
    lis=[i for i in a if l.count(i)>1]
    return (lis)

string=input()
print(duplicate(string))


# In[ ]:


get_ipython().set_next_input('7. Write a Python Program to check if a string contains any special character');get_ipython().run_line_magic('pinfo', 'character')


# In[67]:


import re

def check_string(my_string):

    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(regex.search(my_string) == None):
        print("String does not contains special characters.")
    else:
        print("String contain special character.")

my_string = input("enter your string")
print("The string is :")
print(my_string)
check_string(my_string)


# In[ ]:





# In[ ]:





# In[ ]:




