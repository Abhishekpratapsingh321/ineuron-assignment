#!/usr/bin/env python
# coding: utf-8

# 1. What are escape characters, and how do you use them?

# In[ ]:


In Python strings, the backslash "\" is a special character, also called the "escape" character. 
It is used in representing certain whitespace characters or characters that are illegal in a string.

An escape character is a backslash \ followed by the character you want to insert.


# 2. What do the escape characters n and t stand for?

# In[ ]:


excape character n stands for newline and t stand for tab


# 3. What is the way to include backslash characters in a string?

# In[ ]:


we can include backslash charcters in a string by "\\"


# 4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?

# In[ ]:


The single quote in Howl's is fine because you've used double quotes to mark the beginning and end of the string.


# 5. How do you write a string of newlines if you don't want to use the n character?

# In[ ]:


to write a strig of newlines if we don't want to use the n character the we should use print esach time when we have to get newline
example :-
    print("hello world")
    print("hello world")
    print("hello world")
    print("hello world")


# 6. What are the values of the given expressions?
# 'Hello, world!'[1]
# 'Hello, world!'[0:5]
# 'Hello, world!'[:5]
# 'Hello, world!'[3:]
# 

# In[ ]:


the value of
'Hello, world!'[1] is 'e'
'Hello, world!'[0:5] is 'Hello'
'Hello, world!'[:5] is 'Hello'
'Hello, world!'[3:] is 'lo, world!'


# 7. What are the values of the following expressions?
# 'Hello'.upper()
# 'Hello'.upper().isupper()
# 'Hello'.upper().lower()
# 

# In[ ]:


'Hello'.upper() is 'HELLO'
'Hello'.upper().isupper() is True
'Hello'.upper().lower() is 'hello'


# 8. What are the values of the following expressions?
# 'Remember, remember, the fifth of July.'.split()
# '-'.join('There can only one.'.split())
# 

# In[ ]:


'Remember, remember, the fifth of July.'.split() is ['Remember,', 'remember,', 'the', 'fifth', 'of', 'July.']
'-'.join('There can only one.'.split()) is 'There-can-only-one.'


# 9. What are the methods for right-justifying, left-justifying, and centering a string?

# In[ ]:


The method for right-justifying is rjust(),left-justifying is ljust() and centering is center() a string


# 10. What is the best way to remove whitespace characters from the start or end?

# In[ ]:


strip() is used to remove the whitespace from the start and end both.
rstrip() is used to remove the whitespace from the  end.
lstrip() is used to remove the whitespace from the start.

