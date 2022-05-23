#!/usr/bin/env python
# coding: utf-8

# 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.

# * 
# 'hello'
# -87.8
# - 
# / 
# +	
# 6 
# 

# In[ ]:


values=6,'hello',-87.8
operator=*,-,/,+


# 2. What is the difference between string and variable?

# In[ ]:


A string is a literal text string, i.e. 'Hello'.


# In[ ]:


A variable is something that stores data (per se) - it can store a string, int, float, class, etc.


# 3. Describe three different data types.

# In[ ]:


list:-
      Python Lists are similar to arrays in C. However, the list can contain data of different types. The items stored in the         list are separated with a comma (,) and enclosed within square brackets [].
      
      ex-  list1  = [1, "hi", "Python", 2]    
           print(type(list1))  


# In[ ]:


String:-
    The string can be defined as the sequence of characters represented in the quotation marks.
    In Python, we can use single, double, or triple quotes to define a string.
    
    ex-   str = "this is my string "  
          print(type(str))  


# In[ ]:


Numbers:-
    Number stores numeric values. The integer, float, and complex values belong to a Python Numbers data-type. Python provides       the type() function to know the data-type of the variable. Similarly, the isinstance() function is used to check an object       belongs to a particular class.
    
    ex-   a=9
          print(type(a))
          b=9.5
          print(type(b))
          


# 4. What is an expression made up of? What do all expressions do?

# In[ ]:


An expression is made up a combination of values, variables, operators, and calls to functions.

Expressions are representations of value. They are different from statement in the fact that statements do something while expressions are representation of value. For example any string is also an expressions since it represents the value of the string as well.


# 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?

# In[ ]:


Statements represent an action or command e.g print statements, assignment statements.

Expression is a combination of variables, operations and values that yields a result value.

spam=10 is a statement
spam*spam is an expression 


# 6. After running the following code, what does the variable bacon contain?
# bacon = 22
#   bacon + 1
# 

# In[ ]:


bacon contain 22 as bacon+1 is only an expression it is not assigning new value to bacon


# In[1]:


bacon = 22 
bacon + 1


# In[2]:


bacon


# 7. What should the values of the following two terms be?
# 'spam' + 'spamspam'
# 'spam' * 3
# 

# In[3]:


"spam"+"spamspam"


# In[4]:


"spam"*3


# 8. Why is eggs a valid variable name while 100 is invalid?

# In[ ]:


egg is valid because it starts with an alphabet
and 100 is invalid because it starts with an integer


# 9. What three functions can be used to get the integer, floating-point number, or string version of a value?

# In[11]:


a=10.45
print(int(a))


# In[7]:


a=10
print(float(a))


# In[13]:


a=10
b=str(a)
print(b)
print(type(b))


# 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten ' + 99 + ' burritos.'
# 

# In[ ]:


This expression cause an error because we cannot concatinate a string and integer.
We can only concatenate string with string.

We can fix this by converting 99 to string.


# In[15]:


'I have eaten ' + str(99) + ' burritos.'


# In[ ]:




