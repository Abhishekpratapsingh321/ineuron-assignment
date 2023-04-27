#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('Q1. Can you create a programme or function that employs both positive and negative indexing? Is there any repercussion if you do so');get_ipython().run_line_magic('pinfo', 'so')


# In[6]:


my_list = [1,2,3,4,5,6,6,7,8,9,10]
def bi_index(in_list,position):
    return in_list[position]
print('Positive Indexing ->',bi_index(my_list,5))
print('Negative Indexing ->',bi_index(my_list,-1))


# In[ ]:


Q2. What is the most effective way of starting with 1,000 elements in a Python list? Assume that all elements should be set to the same value.


# In[5]:


start_list = [1 for x in range(1001)] # Quick Way to Create a List Using List Comprehension
print(start_list)


# In[ ]:


Q3. How do you slice a list to get any other part while missing the rest? (For example, suppose you want to make a new list with the elements first, third, fifth, seventh, and so on.)


# In[4]:


my_list = [x for x in range(1,15)]
print(f'my_list -> {my_list}')
sliced_list = my_list[::2]
print(f'sliced_list -> {sliced_list}')


# In[ ]:


Q4. Explain the distinctions between indexing and slicing ?
Ans: Indexing is used when we have to work on index level. While slicing are used over a range of items.


# In[3]:


my_list = [x for x in range(1,15)]
print(f'my_list -> {my_list}')
print(f'Example of indexing -> {my_list[1], my_list[5]}')
print(f'Example of slicing -> {my_list[1:5]}')


# In[ ]:


get_ipython().set_next_input("Q5. What happens if one of the slicing expression's indexes is out of range");get_ipython().run_line_magic('pinfo', 'range')
Ans: If start index is out of range then it will return empty entity.


# In[2]:


my_list = [x for x in range(1,15)]
my_list = [x for x in range(1,15)]
print(f'my_list -> {my_list}')
print(f'Case #1 -> {my_list[20:]}')
print(f'Case #2 -> {my_list[10:100]}')


# In[ ]:


get_ipython().set_next_input('Q6. If you pass a list to a function, and if you want the function to be able to change the values of the list—so that the list is different after the function returns—what action should you do');get_ipython().run_line_magic('pinfo', 'do')
Ans: Always use return statement, if we want the see the changes in the input list.


# In[1]:


my_list = [1,2,3,4,5,6]
def modify_list(in_list):
    in_list.append(200)
    return in_list
print(modify_list(my_list))


# In[ ]:


get_ipython().set_next_input('Q7. What is the concept of an unbalanced matrix');get_ipython().run_line_magic('pinfo', 'matrix')
Ans: In Unbalanced Matrix number of rows is not same as number of columns.

get_ipython().set_next_input('Q8. Why is it necessary to use either list comprehension or a loop to create arbitrarily large matrices');get_ipython().run_line_magic('pinfo', 'matrices')
Ans: List comprehension or a Loop helps creation of large matrices easy. it also helps to implemeent and avoid manual errors. it also makes reading code easy. Also lot of time for manual feeding is reduced.


# In[ ]:





# In[ ]:




