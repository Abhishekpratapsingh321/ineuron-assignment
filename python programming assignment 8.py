#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to Add Two Matrices?

# In[1]:


# Program to add two matrices
# using list comprehension
  
X = [[9,2,3],
    [3,5,6],
    [7 ,1,9]]
  
Y = [[7,8,7],
    [6,9,4],
    [3,5,1]]
 
result = [[X[i][j] + Y[i][j]  for j in range
(len(X[0]))] for i in range(len(X))]
  
for r in result:
    print(r)


# 2. Write a Python Program to Multiply Two Matrices?

# In[2]:


# Program to multiply two matrices
import numpy as np
# take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
# take a 3x4 matrix
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
 
# result will be 3x4
 
result= [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
 
result = np.dot(A,B)
 
for r in result:
    print(r)


# 3. Write a Python Program to Transpose a Matrix?

# In[4]:


# Python3 Program to find
# transpose of a matrix
 
N = 4
 
# This function stores
# transpose of A[][] in B[][]
 
def transpose(A,B):
 
 for i in range(N):
    for j in range(N):
        B[i][j] = A[j][i]
 
 # driver code
A = [ [1, 1, 1, 1],
 [2, 2, 2, 2],
 [3, 3, 3, 3],
 [4, 4, 4, 4]]
 
 
B = A[:][:] # To store result
 
transpose(A, B)
 
print("Result matrix is")
for i in range(N):
    for j in range(N):
        print(B[i][j], " ", end='')
    print()


# 4. Write a Python Program to Sort Words in Alphabetic Order?

# In[6]:


# Function to sort the words in alphabetical
# order
def F(S):
    W = S.split(" ")
    for i in range(len(W)):
        W[i] = W[i].lower()
    W.sort()
 
    # return the sorted words
    return ' '.join(W)
 
# Driver code
S = "Abhishek dsfnknd abdsb dfbv vgb rbn Singh"
print(F(S))


# 5. Write a Python Program to Remove Punctuation From a String?

# In[8]:


# initializing string
test_str = "hello,how are you:? "
 
# printing original string
print("The original string is : " + test_str)
 
# initializing punctuations string
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
# Removing punctuations in string
# Using loop + punctuation string
for ele in test_str:
    if ele in punc:
        test_str = test_str.replace(ele, " ")
 
# printing result
print("The string after punctuation filter : " + test_str)


# In[ ]:




