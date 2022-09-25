#!/usr/bin/env python
# coding: utf-8

# 1. What is the relationship between classes and modules?

# In[ ]:


Basically, a class can be instantiated but a module cannot. A module will never be anything other than a library of methods. 
A class can be so much more -- it can hold its state (by keeping track of instance variables) and 
be duplicated as many times as you want.


# 2. How do you make instances and classes?

# In[ ]:


Call ClassName() to create a new instance of the class ClassName . 
To pass parameters to the class instance, the class must have an __init__() method. 
Pass the parameters in the constructor of the class.


# 3. Where and how should be class attributes created?

# In[ ]:


Class attributes belong to the class itself they will be shared by all the instances. 
Such attributes are defined in the class body parts usually at the top, for legibility.


# 4. Where and how are instance attributes created?

# In[ ]:


Instance attributes are defined in the constructor. Defined directly inside a class. 
Defined inside a constructor using the self parameter. Shared across all objects.


# 5. What does the term "self" in a Python class mean?

# In[ ]:


instance of the class or the pointer
self represents the instance of the class. 
By using the “self” keyword we can access the attributes and methods of the class in python. 
It binds the attributes with the given arguments


# 6. How does a Python class handle operator overloading?

# In[ ]:


To perform operator overloading,
Python provides some special function or magic function that is automatically invoked 
when it is associated with that particular operator. 
For example, when we use + operator, the magic method __add__ is automatically invoked in which 
the operation for + operator is defined


# 7. When do you consider allowing operator overloading of your classes?

# In[ ]:


operator Overloading means giving extended meaning beyond their predefined operational meaning. 
For example operator + is used to add two integers as well as join two strings and merge two lists. 
It is achievable because '+' operator is overloaded by int class and str class


# 8. What is the most popular form of operator overloading?

# In[ ]:


A very popular and convenient example is the Addition (+) operator. 
Just think how the '+' operator operates on two numbers and the same operator operates on two strings. 
It performs “Addition” on numbers whereas it performs “Concatenation” on strings


# 9. What are the two most important concepts to grasp in order to comprehend Python OOP code?

# In[ ]:


inheritance and polymorphism

