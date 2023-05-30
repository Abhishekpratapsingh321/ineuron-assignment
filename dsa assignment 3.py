#!/usr/bin/env python
# coding: utf-8

# # 1.

# In[6]:


def triplet(arr,target):
    diff=float('inf')
    arr.sort()
    for i in range(len(arr)):
        if(i>0 and arr[i]==arr[i-1]):
            continue
        l,r=i+1,len(arr)-1
        while(l<r):
            if(arr[i]+arr[l]+arr[r]==target):
                return target
            elif(abs(arr[i]+arr[l]+arr[r]-target)<diff):
                diff=abs(arr[i]+arr[l]+arr[r]-target)
                ans=arr[i]+arr[l]+arr[r]
            l+=1
            r-=1
    return ans
                
arr=[1,2,3,4,-5]
target=10
triplet(arr,target)


# # 2.

# In[13]:


def foursum(arr,target):
    arr.sort()
    ans=[]
    for i in range(len(arr)):
        if(i>0 and arr[i]==arr[i-1]):
            continue
        for j in range(i+1,len(arr)-1):
            if(j>0 and arr[j]==arr[j-1]):
                continue
            l,r=j+1,len(arr)-1
            while(l<r):
                res=arr[j]+arr[l]+arr[r]+arr[i]
                if(res==target):
                    ans.append([arr[i],arr[j],arr[l],arr[r]])
                    l+=1
                    r-=1
                    while(arr[l]==arr[l-1]):
                        l+=1
                elif(res<target):
                    l+=1
                else:
                    r-=1
                   
    return ans
                
arr=[1,0,-1,0,-2,2]
target=0
foursum(arr,target)


# # 3.

# In[29]:


def nextpermutation(arr):
    if(len(arr)<=1):
        return arr
    i=len(arr)-2
    n=len(arr)
    while(i>=0 and arr[i]>=arr[i+1]):
        i-=1
    if(i>=0):
        j=len(arr)-1
        while(arr[j]<=arr[i]):
            j-=1
        arr[i],arr[j]=arr[j],arr[i]
    arr = arr[:i + 1] + arr[i + 1:][::-1]
    return arr
arr=[2,3,1]
print(nextpermutation(arr))


# # 4.

# In[31]:


def search(arr,target):
    l,r=0,len(arr)-1
    while(l<=r):
        mid=(l+r)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return -1
arr=[1,2,3,4,5,6]
target=7
print(search(arr,target))


# # 5.

# In[33]:


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
digits = [1,2,3]
print(increment(digits))


# # 6.

# In[35]:


def single(arr):
    ans=0
    for i in arr:
        ans=i^ans
    return ans
arr=[2,2,1,1,3]
print(single(arr))


# # 7.

# In[37]:


def inrange(arr,lower,upper):
    arr=arr+[upper+1]
    previous=lower-1
    ans=[]
    for i in arr:
        if i==previous+2:
            ans.append([previous+1,previous+1])
        elif(i>previous+2):
            ans.append([previous+1,i-1])
        previous=i
    return ans
arr=[0,1,3,50,75]
lower,upper=0,99
print(inrange(arr,lower,upper))


# # 8.

# In[39]:


def attend_meeting(arr):
    arr.sort(key=lambda x:x[0])
    for i in range(1,len(arr)):
        if(arr[i-1][1]>arr[i][0]):
            return False
    return True
arr=[[0,5],[5,10],[15,20]]
print(attend_meeting(arr))


# In[ ]:




