#!/usr/bin/env python
# coding: utf-8

# In[96]:


# This program was based on the Saffir-Simpson Hurricane Wind Scale from the National Hurricane
# Center and Central Pacific Hurricane Center. This application demonstrates the use of Nested Conditional.

# Ask the user to type an integer number to know the possible category.
mph=int(input("Welcome! Please type a numeral for the sustained winds(mph) to know the hurricane category: "))
# Variable "mph" will be used to determine the category.
# Used "and" statement and equality symbols to create a range defining the category set.
if mph<=73:
    print("Not classified as a hurricane. To be classified as a Category 1 hurricane has to be at least 74mph.")
elif mph>= 74 and mph<= 95:
        print("Category 1")
elif mph>= 96 and mph <= 110:
            print("Category 2")   
elif mph>= 111 and mph<= 129:
            print("Category 3")       
elif mph>= 130 and mph<= 156:
            print("Category 4")        
else:
    print("Category 5")

