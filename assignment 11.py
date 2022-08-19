#!/usr/bin/env python
# coding: utf-8

# 1. Create an assert statement that throws an AssertionError if the variable spam is a negative
# integer.

# In[ ]:


assert(spam >= 10, 'AssertionError')


# 2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain
# strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are
# considered the same, and 'goodbye' and 'GOODbye' are also considered the same).

# In[ ]:


assert(eggs.lower()==bacon.lower(),"both are same")


# 3. Write an assert statement that always triggers an AssertionError.

# In[ ]:


assert(False,"always trigger an AssertionError")


# 4. What are the two lines that your program must have in order to be able to call logging.debug()?

# In[ ]:


import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    


# 5. What are the two lines that your program must have in order to have logging.debug() send a
# logging message to a file named programLog.txt?

# In[ ]:


import logging
logging.basicConfig(filename="programLog.txt",level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    


# 6. What are the ﬁve logging levels? 

# In[ ]:


DEBUG, INFO, WARNING, ERROR, and CRITICAL


# 7. What line of code would you add to your software to disable all logging messages?

# In[ ]:


logging.disable(logging.CRITICAL)


# 8. Why is using logging messages better than using print() to display the same message?

# In[ ]:


You can disable logging messages without removing the logging function calls. You can selectively disable lower-level logging messages.
Logging messages provides a timestamp.


# 9. What are the differences between the Step, Over, and Out buttons in the Debug Control window? 

# In[ ]:


The Step button will move the debugger into a function call. 
The Over button will quickly execute the function call without stepping into it. 
The Out button will quickly execute the rest of the code until it steps out of the function it currently is in.


# 10. After you click Go in the Debug Control window, when will the debugger stop?

# In[ ]:


By click Go, the debugger will stop when it has reached the end of the program or a line with a breakpoint.


# 11. What is a breakpoint?

# In[ ]:


Breakpoint is a setting on a line of code that causes the debugger to pause when the program execution reaches the line


# 12. How do you set a breakpoint on a line of code in IDLE?

# In[ ]:


set a breakpoint in IDLE, right-click the line and select Set Breakpoint from the context menu.

