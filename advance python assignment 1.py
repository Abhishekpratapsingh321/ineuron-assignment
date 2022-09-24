#!/usr/bin/env python
# coding: utf-8

# 1. What is the purpose of Python's OOP?

# In[ ]:


In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming.


# 2. Where does an inheritance search look for an attribute?

# In[ ]:


All of these objects are namespaces (packages of variables), and the inheritance search is simply a search of the tree from bottom to top looking for the lowest occurrence of an attribute name. Code implies the shape of such trees.


# 3. How do you distinguish between a class object and an instance object?

# In[ ]:


A class is a blueprint which you use to create objects. An object is an instance of a class - it's a concrete 'thing' that you made using a specific class.
So, 'object' and 'instance' are the same thing, but the word 'instance' indicatesthe relationship of an object to its class. This is easy to understand if you look at an example


# 4. What makes the first argument in a class’s method function special?

# In[ ]:


The first parameter in the class method is the class on which you are calling the method, not (necessarily) the class that defines the method. (Having a variable that always holds the same class would probably not be that useful.)


# 5. What is the purpose of the __init__ method?

# In[ ]:


"__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.


# 6. What is the process for creating a class instance?

# In[ ]:


So, all you have to do to create a new instance of a class in Python is choose a name for the object and set it equal to the class name (that you created) followed by ().
When referencing a class in Python, it should always be the class name with parenthesis (). And this is all that is needed to create an instance of a class in Python.


# 7. What is the process for creating a class?

# In[ ]:


Creating a class is as easy as creating a function in Python. In function, we start with the def keyword while class definitions begin with the keyword class.
Following the keyword class, we have the class identifier (i.e. the name of the class we created) and then the : (colon) operator after the class name.

    
#creating a class pratap
class pratap:
    pass


# 8. How would you define the superclasses of a class?

# In[ ]:


I would you define the superclasses of a class with the help of super method

