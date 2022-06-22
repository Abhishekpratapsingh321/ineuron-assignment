#!/usr/bin/env python
# coding: utf-8

# 1. What exactly is []?

# In[ ]:


[] is the empty list that contains no items. 


# 2. In a list of values stored in a variable called spam, how would you assign the value "hello" as the
# third value? (Assume [2, 4, 6, 8, 10] are in spam.)
# In[ ]:


By using insert function we can insert any value at our desired position.
spam=[2,4,6,8,10]
spam.insert(3,"hello")
output: [2,4,6,"hello",8,10]


# Let's pretend the spam includes the list ['a','b','c','d'] for the next three queries.
# 3. What is the value of spam[int(int('3'* 2) / 11)]?

# In[ ]:


spam=['a','b','c','d']
spam[int(int('3'* 2) / 11)]

the above given code give us output 'd'


# 4. What is the value of spam[-1]?

# In[ ]:


The value of spam[-1] is the last element of the list which is 'd'


# 5. What is the value of spam[:2]?

# In[ ]:


the value of spam[:2] is the element starting from 0th index to 2nd index excluding 2nd index
output: 'a','b'


# Let's pretend bacon has the list [3.14,'cat',11,'cat',True] for the next three questions.

# 6. What is the value of bacon.index('cat')?

# In[ ]:


bacon.index('cat') gives output: 1


# 7. How does bacon.append(99) change the look of the list value in bacon?

# In[ ]:


bacon.append(99) 
this code add 99 at th last of bacon list.


# 8. How does bacon.remove('cat') change the look of the list in bacon?

# In[ ]:


bacon.remove('cat') remove the first occuring element 'cat' from the list.


# 9. What are the list concatenation and list replication operators?

# In[ ]:


The list concatenation opeartor is '+'
and the list replication operator is '*'.


# 10. What is difference between the list methods append() and insert()?

# In[ ]:


list method append() adds the element at the last of the list and insert() add the element at the given positon of the list.


# 11. What are the two methods for removing items from a list?

# In[ ]:


the two method of removing the element from list is remove() and pop().


# 12. Describe how list values and string values are identical.

# In[ ]:


Lists are similar to strings, which are ordered collections of characters, except that the elements of a list can have
any type and for any one list, the items can be of different types.


# 13. What's the difference between tuples and lists?

# In[ ]:


The key difference between the tuples and lists is that while the tuples are immutable objects the lists are mutable.
This means that tuples cannot be changed while the lists can be modified.


# 14. How do you type a tuple value that only contains the integer 42?

# In[ ]:


l=(42,)
type(l)


# 15. How do you get a list value's tuple form? How do you get a tuple value's list form?

# In[ ]:


we can get list value's tuple form by using type conversion using tuple()
we can get tuple value's list form by using type conversion using list()


# 16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they
# contain?

# In[ ]:


Variables will contain references to list values rather than list values themselves.
But for strings and integer values, variables simply contain the string or integer value.


# 17. How do you distinguish between copy.copy() and copy.deepcopy()?

# In[ ]:


copy() create reference to original object. If you change copied object - you change the original object.
.deepcopy() creates new object and does real copying of original object to new one. Changing new deepcopied object doesn't affect original object.

