#!/usr/bin/env python
# coding: utf-8

# 1. Assign the value 7 to the variable guess_me. Then, write the conditional tests (if, else, and elif) to
# print the string 'too low' if guess_me is less than 7, 'too high' if greater than 7, and 'just right' if equal
# to 7.

# In[ ]:


guess_me = 7
if guess_me < 7:
    print("too low")
elif guess_me > 7:
    print("too high")
else:
    print("just right")
print_footer(section)


# 2. Assign the value 7 to the variable guess_me and the value 1 to the variable start. Write a while
# loop that compares start with guess_me. Print too low if start is less than guess me. If start equals
# guess_me, print'found it!'; and exit the loop. If start is greater than guess_me, print 'oops' and exit
# the loop. Increment start at the end of the loop.

# In[ ]:


start,guess_me=1,7
while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    start += 1


# 3. Print the following values of the list [3, 2, 1, 0] using a for loop.

# In[ ]:


l=[3,2,1,0]
for i in l:
    print(i)


# 4. Use a list comprehension to make a list of the even numbers in range(10)

# In[ ]:


l=[i for i in range(1,10) if i%2==0]
l


# 5. Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the
# keys, and use the square of each key as its value.

# In[5]:


l={i:i**2 for i in range(10)}
l


# 6. Construct the set odd from the odd numbers in the range using a set comprehension (10).

# In[6]:


l={i for i in range(10) if i%2 != 0}
l


# 7. Use a generator comprehension to return the string 'Got' and a number for the numbers in
# range(10). Iterate through this by using a for loop.

# In[7]:


for i in range(10):
    print("Got", i)


# 8. Define a function called good that returns the list ['Harry', 'Ron', 'Hermione'].

# In[9]:


def good():
    return ['Harry', 'Ron', 'Hermione']
    
    


# 9. Define a generator function called get_odds that returns the odd numbers from range(10). Use a
# for loop to find and print the third value returned.

# In[11]:


def get_odds():
     return [i for i in range(10) if i%2!=0]
l=get_odds()
for i in range(len(l)):
    if i==2:
        print(l[i])
        break


# 10. Define an exception called OopsException. Raise this exception to see what happens. Then write
# the code to catch this exception and print 'Caught an oops'.

# In[12]:


class OopsException(Exception):
    pass


def with_exception(a):
    if a < 0:
        raise OopsException(a)


try:
    with_exception(-1)
except OopsException as err:
    print('Caught an oops')


# 11. Use zip() to make a dictionary called movies that pairs these lists: titles = ['Creature of Habit',
# 'Crewel Fate'] and plots = ['A nun turns into a monster', 'A haunted yarn shop'].

# In[13]:


titles = ['Creature of Habit','Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = {}
for title, plot in zip(titles, plots):
    movies = dict(zip(titles, plots))
print(movies)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




