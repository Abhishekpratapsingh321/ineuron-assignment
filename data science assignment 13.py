#!/usr/bin/env python
# coding: utf-8

# 1. What advantages do Excel spreadsheets have over CSV spreadsheets?
# 

# In[ ]:


Reading large data set is much easier for the end-user to read, comprehend and understand when compared to CSV.
Excel also provides the user option for external linking of data from other sources, and also, the user can do custom add-ins.


# 2. What do you pass to csv.reader() and csv.writer() to create reader and writer objects?

# In[ ]:


Write:- First, we call open() and pass it 'w' to open a file in write mode . This will create the object you can then pass to csv.writer() to create a Writer object.
Read:- First, we call open() and pass it 'r' to open a file in write mode . This will create the object you can then pass to csv.reader() to create a Reader object.


# 3. What modes do File objects for reader and writer objects need to be opened in?
# 

# In[ ]:


we must use the built-in open() function. The open() function uses two arguments. First is the name of the file and second is for what purpose we want to open it .
And for reader we use 'r' and for writer we use 'w'.


# 4. What method takes a list argument and writes it to a CSV file?
# 

# In[ ]:


writerows(), this method takes list as a argument aand writes it to a csv file.


# 5. What do the keyword arguments delimiter and line terminator do?

# In[ ]:


The delimiter is the character that appears between cells on a row. By default, the delimiter for a CSV file is a comma, it separate two value
The line terminator is the character that comes at the end of a row. By default, the line terminator is a newline. 


# 6. What function takes a string of JSON data and returns a Python data structure?

# In[ ]:


json.loads() method return Python data structure of JSON string or data.


# 7. What function takes a Python data structure and returns a string of JSON data?

# In[ ]:


get_ipython().set_next_input('json.dumps() function takes a Python data structure and returns a string of JSON data');get_ipython().run_line_magic('pinfo', 'data')

