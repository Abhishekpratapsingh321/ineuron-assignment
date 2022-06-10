#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Why are functions advantageous to have in your programs');get_ipython().run_line_magic('pinfo', 'programs')


# In[ ]:


Functions reduces the need for duplicate code. This makes programs shorter, easier to read, and easier to update.


# In[ ]:


get_ipython().set_next_input("2. When does the code in a function run: when it's specified or when it's called");get_ipython().run_line_magic('pinfo', 'called')


# In[ ]:


The code in a function run when it is called.


# In[ ]:


get_ipython().set_next_input('3. What statement creates a function');get_ipython().run_line_magic('pinfo', 'function')


# In[ ]:


You start a function with the def keyword, specify a name followed by a colon (:) sign.
The “def” call creates the function object and assigns it to the name given. 
You can further re-assign the same function object to other names.


# In[1]:


def print_my_name():
    print("My name is pratap")
print_my_name()    


# In[ ]:


get_ipython().set_next_input('4. What is the difference between a function and a function call');get_ipython().run_line_magic('pinfo', 'call')


# In[ ]:


Function:-A function is a piece of code which enhanced the reusability and modularity of your program.It means that piece of 
    code need not be written again.
Function call:-A function call means invoking or calling that function. Unless a function is called there is no use of that 
    function.
    


# In[ ]:


get_ipython().set_next_input('5. How many global scopes are there in a Python program? How many local scopes');get_ipython().run_line_magic('pinfo', 'scopes')


# In[ ]:


There is only one global Python scope per program execution. 
There is many local scope in python


# In[ ]:


get_ipython().set_next_input('6. What happens to variables in a local scope when the function call returns');get_ipython().run_line_magic('pinfo', 'returns')


# In[ ]:


A local variable retains its value until the next time the function is called A local variable becomes undefined after the function 
call completes.The local variable can be used outside the function any time after the function call completes. 


# In[ ]:


get_ipython().set_next_input('7. What is the concept of a return value? Is it possible to have a return value in an expression');get_ipython().run_line_magic('pinfo', 'expression')


# In[ ]:


A return is a value that a function returns to the calling script or function when it completes its task. A return value can be any one of the four variable types:
handle, integer, object, or string. The type of value your function returns depends largely on the task it performs.

Yes, it is possible to have areturn value in an expression.


# In[ ]:


get_ipython().set_next_input('8. If a function does not have a return statement, what is the return value of a call to that function');get_ipython().run_line_magic('pinfo', 'function')


# In[ ]:


If a function does not specify a return value, it returns None.


# In[ ]:


get_ipython().set_next_input('9. How do you make a function variable refer to the global variable');get_ipython().run_line_magic('pinfo', 'variable')


# In[ ]:


If you want to refer to a global variable in a function, you can use the global keyword to declare which variables are global.


# In[ ]:


get_ipython().set_next_input('10. What is the data type of None');get_ipython().run_line_magic('pinfo', 'None')


# In[ ]:


None is used to define a null value. It is not the same as an empty string, False, or a zero. 
It is a data type of the class NoneType object. 


# In[ ]:


get_ipython().set_next_input('11. What does the sentence import areallyourpetsnamederic do');get_ipython().run_line_magic('pinfo', 'do')


# In[ ]:


That import statement imports a module named areallyourpetsnamederic.


# In[ ]:


get_ipython().set_next_input('12. If you had a bacon() feature in a spam module, what would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')


# In[ ]:


This function can be called with spam.bacon()


# In[ ]:


get_ipython().set_next_input('13. What can you do to save a programme from crashing if it encounters an error');get_ipython().run_line_magic('pinfo', 'error')


# In[ ]:


When it encounters an error, the control is passed to the except block, skipping the code in between. As seen in the above code,
we have moved our code inside a try and except statement. 
Try running the program and it should throw an error message instead of crashing the program.


# In[ ]:


get_ipython().set_next_input('14. What is the purpose of the try clause? What is the purpose of the except clause');get_ipython().run_line_magic('pinfo', 'clause')


# In[ ]:


The try block allows you to test a block of code for errors. 
The except block enables you to handle the error with a user-defined response.

