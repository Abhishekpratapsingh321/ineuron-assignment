#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to Find LCM?
# 

# In[ ]:


def lcm(num1,num2):
    if num1>num2:
        greater=num1
    else:
        greater=num2
    while True:
        
        if greater%num1==0 and greater%num2==0:
            return greater 
        else:
            greater=greater+1
    

num = list(map(int, input("Enter multiple values: "). split()))
num1=num[0]
num2=num[1]
lcmis=lcm(num1,num2)
for i in range(2,len(num)):
    lcmis=lcm(num[i],lcmis)
    
print(lcmis)    


# 2. Write a Python Program to Find HCF?
# 

# In[ ]:


def hcf(num1,num2):
    if num1%num2==0:
        return num2
    else:
        return hcf(num2,num1%num2)
num = list(map(int, input("Enter multiple values: "). split()))
num1=num[0]
num2=num[1]
hcfis=hcf(num1,num2)
for i in range(2,len(num)):
    hcfis=hcf(num[i],hcfis)
    
print(hcfis)            


# In[ ]:


get_ipython().set_next_input('3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal');get_ipython().run_line_magic('pinfo', 'Hexadecimal')


# In[ ]:


# Python program to convert decimal into other number systems
dec=int(input("enter the decimal no."))

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


# In[ ]:


get_ipython().set_next_input('4. Write a Python Program To Find ASCII value of a character');get_ipython().run_line_magic('pinfo', 'character')


# In[ ]:


# Program to find the ASCII value of the given character

c =input("enter your character")
print("The ASCII value of '" + c + "' is", ord(c))


# In[ ]:


get_ipython().set_next_input('5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations');get_ipython().run_line_magic('pinfo', 'operations')


# In[ ]:


def sum(a,b):
    ans=a+b
    print(ans)
def sub(a,b):
    ans=a-b
    print(ans)
def mul(a,b):
    ans=a*b
    print(ans)
def div(a,b):
    ans=a/b
    print(ans)

a=int(input("enter your first no."))
b=int(input("enter your second no."))
c=int(input("enter 1 for add, 2 for subtract, 3 for divison, 4 for multplication"))
if c==1:
    sum(a,b)
elif c==2:
     sub(a,b)
elif c==3:
    div(a,b)
elif c==4:
    mul(a,b)    
    
    


# In[ ]:




