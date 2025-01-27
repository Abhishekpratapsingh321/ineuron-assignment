#!/usr/bin/env python
# coding: utf-8

# Q1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# You can return the answer in any order.
# 
# Example: Input: nums = [2,7,11,15], target = 9 Output0 [0,1]
# 
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

# In[1]:


def twosum(arr,target):
    res={}
    for i,n in enumerate(arr):
        diff = target-n
        if diff in res:
            return [i,res[diff]]
        else:
            res[n]=i
    return ans
nums = [2,7,9,7,3,6,11,2,15] 
target = 9 
print(twosum(nums,target))


# Q2. Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# 
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# 
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Example : Input: nums = [3,2,2,3], val = 3 Output: 2, nums = [2,2,*,*]
# 
# Explanation: Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores)[

# In[2]:


def remove(nums,target):
    i = 0
    for x in nums:
        if x != target:
            nums[i] = x
            i += 1
    for i in range(i,len(nums)):
        nums[i]="_"
    return nums
arr=[0,1,2,2,3,0,4,2]
target=2
print(remove(arr,target))


# Q3. Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# Example 1: Input: nums = [1,3,5,6], target = 5
# 
# Output: 2

# In[3]:


def binary(arr,target):
    l,r=0,len(arr)-1
    mid=(1+r)//2
    while l<r:
        if arr[mid]==target:
            return arr[mid]
        elif arr[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return 0
nums = [1,3,5,6]
target = 7
print(binary(nums,target))


# Q4. You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# 
# Increment the large integer by one and return the resulting array of digits.
# 
# Example 1: Input: digits = [1,2,3] Output: [1,2,4]
# 
# Explanation: The array represents the integer 123.
# 
# Incrementing by one gives 123 + 1 = 124. Thus, the result should be [1,2,4].

# In[4]:


def increment(arr):
    for i in range(len(arr)-1,0,-1):
        if (arr[i]<9):
            arr[i]+=1
            return arr
        else:
            arr[i]=0
    result = [0] * (len(arr) + 1)
    result[0]=1
    return result
digits = [9,9,9]
print(increment(digits))


# Q5. You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# 
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# 
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# 
# Example 1: Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 Output: [1,2,2,3,5,6]
# 
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6]. The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# In[5]:


def merge(arr1,arr2,m,n):
    l=m+n-1
    while n>0 and m>0:
        if arr1[m-1]>=arr2[n-1]:
            arr1[l]=arr1[m-1]
            m-=1
        else:
            arr1[l]=arr2[n-1]
            n-=1
        l-=1
    while n>0:
        arr1[l]=arr2[n-1]
        n,l=n-1,l-1
    return arr1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3 
print(merge(nums1,nums2,m,n))


# Q6. Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# 
# Example 1: Input: nums = [1,2,3,1]
# 
# Output: true
# 
# 

# In[6]:


def twice(arr):
    l=set()
    for i in range(len(arr)):
        if arr[i] in l:
            return True
        l.add(arr[i])
    return False
nums = [1,2,3,3,5]
print(twice(nums))


# Q7. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.
# 
# Note that you must do this in-place without making a copy of the array.
# 
# Example 1: Input: nums = [0,1,0,3,12] Output: [1,3,12,0,0]

# In[7]:


def shift(arr):
    l=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[l]=arr[i]
            l+=1
    while l<len(arr):
        arr[l]=0
        l+=1
    return arr
nums = [0,1,0,3,7,12] 
print(shift(nums))


# Q8. You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
# 
# You are given an integer array nums representing the data status of this set after the error.
# 
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
# 
# Example 1: Input: nums = [1,2,2,4] Output: [2,3]

# In[8]:


def findErrorNums(nums):
    length=len(nums) 
    sum_nums = length*(length+1)//2 #Sum of first n positive integers = n(n + 1)/2 
    repetition = sum(nums) - sum(set(nums))
    loss = sum_nums - sum(set(nums))
    return [repetition,loss]
nums = [1,2,2,4]
print(findErrorNums(nums))


# In[ ]:




