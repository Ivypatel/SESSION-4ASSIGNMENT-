#!/usr/bin/env python
# coding: utf-8

# In[1]:


PI = 3.14
radius = float(input(' Please Enter the radius of a circle: '))

diameter = 2 * radius
circumference = 2 * PI * radius
area = PI * radius * radius

print(" \nDiameter Of a Circle = %.2f" %diameter)
print(" Circumference Of a Circle = %.2f" %circumference)
print(" Area Of a Circle = %.2f" %area)


# In[2]:


number = int(input(" Please Enter any Positive Integer : "))
exponent = int(input(" Please Enter Exponent Value : "))
power = 1

for i in range(1, exponent + 1):
    power = power * number
    
print("The Result of {0} Power {1} = {2}".format(number, exponent, power))


# In[3]:


# input age
age = int(input("Enter Age : "))

# condition to check voting eligibility
if age>=18:
        status="Eligible"
else:
    status="Not Eligible"

print("You are ",status," for Vote.")


# In[4]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))


# In[5]:


def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(12))


# In[6]:


length = float(input('Please Enter the Length of a Triangle: '))
width = float(input('Please Enter the Width of a Triangle: '))

# calculate the perimeter
perimeter = 2 * (length + width)

print("Perimeter of a Rectangle using", length, "and", width, " = ", perimeter)


# In[ ]:




