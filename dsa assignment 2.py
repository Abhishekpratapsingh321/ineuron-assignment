#!/usr/bin/env python
# coding: utf-8

# **Question 1**
# 
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
# 
# **Example 1:**
# 
# Input: nums = [1,4,3,2]
# Output: 4
# 
# **Explanation:**
# 
# All possible pairings (ignoring the ordering of elements) are:
# 
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# So the maximum possible sum is 4

# In[2]:


def array(arr):
    arr.sort()
    sum=0
    for i in range(0,len(arr),2):
        sum+=arr[i]
    return sum
arr=[1,4,3,2] 
print(array(arr))


# Question 2
# 
# Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor. 
# 
# The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice. 
# 
# Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.
# 
# Example 1:
# 
# Input: candyType = [1,1,2,2,3,3]
# 
# Output: 3
# 
# Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.

# In[4]:


def array(arr):
    a=set(arr)
    ans=min(len(a),len(arr)//2)
    return ans
arr=[1,1,2,3]
print(array(arr))


# Question 3
# 
# We define a harmonious array as an array where the difference between its maximum value
# and its minimum value is exactly 1.
# 
# Given an integer array nums, return the length of its longest harmonious subsequence
# among all its possible subsequences.
# 
# A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
# 
# Example 1:
#     
# Input: nums = [1,3,2,2,5,2,3,7]
#     
# Output: 5
# 
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].

# In[20]:


def array(arr):
    a={}
    for i in arr:
        a[i]=1+a.get(i,0)
    maxhl=0
    for i in a:
        
        if (i+1) in a:
            maxhl=max(a[i]+a[i+1],maxhl)
        
    return maxhl 
nums = [1,3,2,2,5,2,3,7]
print(array(nums))


# In[ ]:


Question 4

You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
    
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true


# In[24]:


def canPlaceFlowers(flowerbed, n):
    total=0
    i=0
    while(i<len(flowerbed) and total<n):
        if(flowerbed[i]==0):
            nextf = 0 if i==len(flowerbed)-1 else flowerbed[i]
            prevf= 0 if (i==0) else flowerbed[i-1]
            if nextf==0 and prevf==0:
                flowerbed[i]=1
                total+=1
        i+=1 
    
    return total==n

flowerbed = [1,0,0,0,1]
n = 1
print(canPlaceFlowers(flowerbed, n))


# In[ ]:


Question 5
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6


# In[27]:


def product(arr):
    res=1
    curmax,curmin=1,1
    for i in arr:
        temp=curmax*i
        curmax=max(i*curmax,i*curmin,i)
        curmin=min(i*temp,i*curmin,i)
        res=max(curmax,curmin)
    return res
nums = [-2,4,2,3]
print(product(nums))


# In[ ]:


Question 6
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise,
return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Explanation: 9 exists in nums and its index is 4


# In[37]:


def binsearch(arr,target):
    l,r=0,len(arr)-1
    while(l<=r):
        mid=(l+r)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l=mid+1
        else:
            r=mid-1
            
nums = [-1,0,3,4,5,9,12]
target = 4
print(binsearch(nums,target))


# In[ ]:


Question 7

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:
    
Input: nums = [1,2,2,3]
    
Output: true


# In[43]:


def monotone(arr):
    i=0
    if arr[i]<arr[i+1]:
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                return False
    else:
        for i in range(len(arr)-1):
            if arr[i]<arr[i+1]:
                return False
    return True
nums = [1,2,3,2,3,1]
print(monotone(nums))


# In[ ]:


Question 8
You are given an integer array nums and an integer k.

In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum score of nums after applying the mentioned operation at most once for each index in it.

Example 1:
Input: nums = [1], k = 0
Output: 0

Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.


# In[49]:


def min_max(arr,k):
    i=0
    min_val,max_val=arr[i],arr[i]
    for i in range(1,len(arr)):
        min_val=min(arr[i],min_val)
        max_val=max(arr[i],max_val)
    if (min_val + k > max_val - k):
        return 0
    else:
        return (max_val-k) - (min_val+k)

nums = [1]
k = 0 
print(min_max(nums,k))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




