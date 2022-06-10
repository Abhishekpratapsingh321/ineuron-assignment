#!/usr/bin/env python
# coding: utf-8

# 1. Why are functions advantageous to have in your programs?

# In[ ]:


Functions reduces the need for duplicate code. This makes programs shorter, easier to read, and easier to update.


# 2. When does the code in a function run: when it's specified or when it's called?

# In[ ]:


The code in a function run when it is called.


# 3. What statement creates a function?

# In[ ]:


You start a function with the def keyword, specify a name followed by a colon (:) sign.
The “def” call creates the function object and assigns it to the name given. 
You can further re-assign the same function object to other names.


# In[1]:


def print_my_name():
    print("My name is pratap")
print_my_name()    


# 4. What is the difference between a function and a function call?

# In[ ]:


Function:-A function is a piece of code which enhanced the reusability and modularity of your program.It means that piece of 
    code need not be written again.
Function call:-A function call means invoking or calling that function. Unless a function is called there is no use of that 
    function.
    


# 5. How many global scopes are there in a Python program? How many local scopes?

# In[ ]:


There is only one global Python scope per program execution. 
There is many local scope in python


# 6. What happens to variables in a local scope when the function call returns?

# In[ ]:


A local variable retains its value until the next time the function is called A local variable becomes undefined after the function 
call completes.The local variable can be used outside the function any time after the function call completes. 


# 7. What is the concept of a return value? Is it possible to have a return value in an expression?

# In[ ]:


A return is a value that a function returns to the calling script or function when it completes its task. A return value can be any one of the four variable types:
handle, integer, object, or string. The type of value your function returns depends largely on the task it performs.

Yes, it is possible to have areturn value in an expression.


# 8. If a function does not have a return statement, what is the return value of a call to that function?

# In[ ]:


If a function does not specify a return value, it returns None.


# 9. How do you make a function variable refer to the global variable?

# In[ ]:


If you want to refer to a global variable in a function, you can use the global keyword to declare which variables are global.


# 10. What is the data type of None?

# In[ ]:


None is used to define a null value. It is not the same as an empty string, False, or a zero. 
It is a data type of the class NoneType object. 


# 11. What does the sentence import areallyourpetsnamederic do?

# In[ ]:


That import statement imports a module named areallyourpetsnamederic.


# 12. If you had a bacon() feature in a spam module, what would you call it after importing spam?

# In[ ]:


This function can be called with spam.bacon()


# 13. What can you do to save a programme from crashing if it encounters an error?

# In[ ]:


When it encounters an error, the control is passed to the except block, skipping the code in between. As seen in the above code,
we have moved our code inside a try and except statement. 
Try running the program and it should throw an error message instead of crashing the program.


# 14. What is the purpose of the try clause? What is the purpose of the except clause?

# In[ ]:


The try block allows you to test a block of code for errors. 
The except block enables you to handle the error with a user-defined response.

