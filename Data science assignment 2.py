#!/usr/bin/env python
# coding: utf-8

# 1.What are the two values of the Boolean data type? How do you write them?

# In[ ]:


True and False are two values of boolean data type.
we write them as True and False. 


# 2. What are the three different types of Boolean operators?

# In[ ]:


The 3 different types of boolean operators are "AND","OR","NOT".


# 3. Make a list of each Boolean operator(i.e. every possible combination of Boolean
# values for the operator and what it evaluate ).

# In[1]:


True and True


# In[2]:


True and False


# In[3]:


False and True


# In[4]:


False and False


# In[5]:


True or True


# In[6]:


True or False


# In[7]:


False or False 


# In[8]:


False or True


# In[9]:


not True


# In[10]:


not False


# 4. What are the values of the following expressions?
# (5 > 4) and (3 == 5)
# not (5 > 4)
# (5 > 4) or (3 == 5)
# not ((5 >4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)

# In[11]:


(5 > 4) and (3 == 5)


# In[12]:


not (5 > 4) 


# In[14]:


(5 > 4) or (3 == 5) 


# In[15]:


not ((5 >4) or (3 == 5))


# In[17]:


(True and True) and (True == False)


# In[18]:


(not False) or (not True)


# 5. What are the six comparison operators?

# In[ ]:


1. Equal-To (== )


# In[ ]:


2. Not-Equal-To (!= )


# In[ ]:


3. Greater-Than (> )


# In[ ]:


4. Less-Than (< )


# In[ ]:


5. Greater-Than-Equal-To (>= )


# In[ ]:


6. Less-Than-Equal-To (<= )


# 6. How do you tell the difference between the equal to and assignment operators?Describe a
# condition and when you would use one.

# In[ ]:


equal (==) to operator is used when we have to compare to value i.e they are equal or not
assignment operator (=) is used to assign right hand side valuse to left hand side


# In[ ]:


7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print(&#39;eggs&#39;)
if spam &gt; 5:
print(&#39;bacon&#39;)
else:
print(&#39;ham&#39;)
print(&#39;spam&#39;)
print(&#39;spam&#39;)


# In[ ]:


if spam==10:
    print("eggs")
this is first block
if spam>5:
    print("bacon")
this is second block
else:
    print("ham")
    print("spam")
    print("spam")
this is third block    


# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
# Greetings! if anything else is stored in spam.

# In[ ]:


spam=0
if spam==1:
    print("Hello")
elif spam==2:
    print("spam")
else:
    print("Greetings!")


# 9.If your programme is stuck in an endless loop, what keys you’ll press?

# In[ ]:


If your programme is stuck in an endless loop then we will press "ctrl+c" press key.


# 10. How can you tell the difference between break and continue?

# In[ ]:


break statement terminates the smallest enclosing loop (i.e., while, do-while, for loop, or switch statement).


# In[ ]:


continue statement skips the rest of the loop statement and starts the next iteration of the loop to take place


# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

# In[ ]:


range(10): it means in for loop that returns a sequence of no. from default value 0 to 9.
range(0,10): it means in for loop that returns a sequence of no. from  0 to 9.
range(0,10,1): it means in for loop that returns a sequence of no. from  0 to 9 by skipping 1 no.


# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
# program that prints the numbers 1 to 10 using a while loop.

# In[21]:


for i in range(1,11):
    print(i,end="  ")


# In[23]:


i=1
while i<11:
    print(i,end="  ")
    i+=1


# 13. If you had a function named bacon() inside a module named spam, how would you call it after
# importing spam?

# In[ ]:


we will call that function from spam.bacon()

