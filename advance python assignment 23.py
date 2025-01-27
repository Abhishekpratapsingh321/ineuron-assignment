#!/usr/bin/env python
# coding: utf-8
Q1. If you have any, what are your choices for increasing the comparison between different figures on the same graph?

Ans: Matplotlib provides a convenient method called subplots for increasing the comparison between different figures on the same graph. Subplots mean a group of smaller axes (where each axis is a plot) that can exist together within a single figure.
# In[1]:


import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()

Q2. Can you explain the benefit of compound interest over a higher rate of interest that does not compound after reading this chapter?

Ans: Compound interest makes a sum of money grow at a faster rate than simple interest,because in addition to earning returns on the money you invest, you also earn returns on those returns at the end of every compounding period, which could be daily, monthly, quarterly or annually.



Q3. What is a histogram, exactly? Name a numpy method for creating such a graph ?

Ans: Histogram shows total values of X wrt Y. Which means at any particular position of X, Y value shows the total number of counts or data below that value of X. numpy.histogram() is the built in function used.



Q4. If necessary, how do you change the aspect ratios between the X and Y axes ?

Ans: We can use figure(figsize=(10,8)) function inside the matplot.pyplot library which we scale down or up the graph.



Q5. Compare and contrast the three types of array multiplication between two numpy arrays: dot product, outer product, and regular multiplication of two numpy arrays ?

Ans: :

    a. In regular multiplication values of same index get multiplied.
    b. In dot product there is row wise multiplication, row of one array with column of second array and so on.
    c. In outer multiplication every element of first array a1 will be multiply by every element of other array a2 such such the        number of columns will be equal to the number of element in another array a2.


Q6. Before you buy a home, which numpy function will you use to measure your monthly mortgage payment ?

Ans: np.pmt(rate, nper, pv) function we will be using in order to calculate monthly mortgage payment before you purchase a house.


     rate = The periodic interest rate
     nper = The number of payment periods
     pv = The total value of the mortgage loan
     

Q7. Can string data be stored in numpy arrays? If so, list at least one restriction that applies to this data ?

Ans: Yes, an array can store the string. The limitation which imposed on the string data is, whenever we store the data of string dtype then we should keep in mind that the string which is having the maximum length will become the limit. Below example demonstrates that when New Zealand is added then it takes only 'New Z' because limit is set as 5 before.



# In[2]:


# importing numpy as np
import numpy as np
  
# Create the numpy array
country = np.array(['USA', 'Japan', 'UK', '', 'India', 'China'])
  
# Print the array
print(country)

# Assign 'New Zealand' at the place of missing value
country[country == ''] = 'New Zealand'
  
# Print the modified array
print(country)


# In[ ]:




