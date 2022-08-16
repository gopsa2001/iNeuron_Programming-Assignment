#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 1. Write a Python program to convert kilometers to miles?
n=int(input("give km value : "))
print("in miles : ", n*0.621371)


# In[6]:


# 2. Write a Python program to convert Celsius to Fahrenheit?
C=int(input("give celsius value : "))
print("in fahrenheit : ",(C * 9/5) + 32)


# In[10]:


# 3. Write a Python program to display calendar?
import calendar
n=int(input(" press 1 for whole calendar of a year or press 2 for particular month in a year : "))
if n==1:
    y=int(input("input year : "))
    print(calendar.calendar(y))
if n==2:
    y=int(input("input year : "))
    m=int(input("input month as numeric : "))
    print(calendar.month(y,m))
    
    


# In[5]:


# 4. Write a Python program to solve quadratic equation?
import math
a=int(input("give value of 'a' :"))
b=int(input("give value of 'b' :"))
c=int(input("give value of 'c' :"))
print("first root is : ", (-(b)+math.sqrt((b**2)-4*a*c))/2*a)
print("first root is : ", (-(b)-math.sqrt((b**2)-4*a*c))/2*a)


# In[7]:


# 5. Write a Python program to swap two variables without temp variable?
a=int(input("input value of 'a' : "))
b=int(input("input value of 'b' : "))
a=a+b
b=a-b
a=a-b
print("value of 'a' is : ",a," value of 'b' is : ",b)

