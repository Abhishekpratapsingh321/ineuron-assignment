#!/usr/bin/env python
# coding: utf-8

# 1. To what does a relative path refer?

# In[ ]:


A relative file path is interpreted from the perspective your current working directory or we describe the path with respect to current working directory.


# 2. What does an absolute path start with your operating system?

# In[ ]:


The absolute path will begin at the home directory of our computer and will end with the file or directory that we wish to access.


# 3. What do the functions os.getcwd() and os.chdir() do?

# In[ ]:


os.getcwd() helps us to see the current working dirctory.
os.chdir() allow us to set the current working directory to a path of your choice.


# 4. What are the . and .. folders?

# In[ ]:


single dot (".") refers to current directory.
double dot ("..") refers to move up in hierarchy from the current directory.


# 5. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?

# In[ ]:


C:\bacon\eggs is a dir name and spam.txt is a base name.


# 6. What are the three “mode” arguments that can be passed to the open() function?

# In[ ]:


the three mode of arguments that can be passed to the open() function are 
r - open a file in read mode. w - opens or create a text file in write mode. a - opens a file in append mode.


# 7. What happens if an existing file is opened in write mode?

# In[ ]:


if an existing file is opened in write mode then its contents are discarded and the file is treated as a new empty file.


# 8. How do you tell the difference between read() and readlines()?

# In[ ]:


The main difference is that read() will read the whole file at once and then print out the first characters that take up as many
bytes as you specify in the parenthesis versus the readline() that will read and print out only the first characters that take 
up as many bytes as you specify in the parenthesis


# 9. What data structure does a shelf value resemble?

# In[ ]:


A shelf value resembles a dictionary value; it has keys and values, along with keys() and values() methods that work similarly 
to the dictionary methods of the same names.

