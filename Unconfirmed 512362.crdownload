#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to Extract Unique values dictionary values?

# In[ ]:


my_dict = {'hi' : [5,3,8, 0],
   'there' : [22, 51, 63, 77],
   'how' : [7, 0, 22],
   'are' : [12, 11, 45],
   'you' : [56, 31, 89, 90]}

my_result = list(sorted({elem for val in my_dict.values() for elem in val}))

print(my_result)


# 2.	Write a Python program to find the sum of all items in a dictionary?

# In[ ]:


dic={ 'x':455, 'y':223, 'z':300, 'p':908 }

print("sum: ",sum(dic.values()))


# 3.	Write a Python program to Merging two Dictionaries?

# In[ ]:


dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print(dict_1 | dict_2)


# 4.	Write a Python program to convert key-values list to flat dictionary?

# In[ ]:


dic= { "day": [1, 2, 3], "name": ['Mon', 'Tues', 'Wed' ] }

f_dic= dict(zip(dic["day"], dic["name"]))
print("FLATTENED DICTIONARY: ", f_dic)


# 5.	Write a Python program to insertion at the beginning in OrderedDict?

# In[ ]:


from collections import OrderedDict
dic1 = OrderedDict([('A', '100'), ('B', '200'), ('C', '300')])
insrt = OrderedDict([("D", '400')])
  
final = OrderedDict(list(insrt.items()) + list(dic1.items()))
  
# print result
print ("Resultant Dictionary :")
print(final)


# 6.	Write a Python program to check order of character in string using OrderedDict()?

# In[ ]:


from collections import OrderedDict 
def checkOrder(string, pattern): 
    dic = OrderedDict.fromkeys(string) 
    ptr = 0
    for key,value in dic.items(): 
        if (key == pattern[ptr]): 
            ptr = ptr + 1
        if (ptr == (len(pattern))): 
            return 'True'
    return 'False'

string = 'Study tonight'
pattern = 'stu'
print (checkOrder(string,pattern))

string2= 'Welcome'
pattern2= 'cm'
print (checkOrder(string2,pattern2)) 


# 7.	Write a Python program to sort Python Dictionaries by Key or Value?

# In[ ]:


key_value={1:2 ,2:1 ,4:3 ,3:4 ,6:5 ,5:6 }

# sorted by key
for i in sorted(key_value) :
    print ((i, key_value[i]), end =" ")


# In[ ]:


#sorted by value
print(sorted(key_value.items(), key=lambda keyval: (keyval[1], keyval[0])))


# In[ ]:




