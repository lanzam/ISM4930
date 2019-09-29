#!/usr/bin/env python
# coding: utf-8

# In[7]:


# This program will save the phone number of the user and in case the user 
# wants to add an additional phone number it will be asked and 
#This application demonstrates the use of iteration with the DO WHILE LOOP.

# Ask the use user to type their phone number
num=int(input("Please type your phone number:")) 
print("The phone number added to the list is:",num)
#If the user would like to add another phone number
add=input("Would you like to add an additional phone numbers? Type yes or no")
# WHILE LOOP. Variable "add" will if user types only "yes" in case of an 
# additional number.
while add=="yes":
#If the user types "yes", then add an additional number
    num=int(input("Enter your phone number:"))
    print("The number entered is:",num)
    add=input("Would you like to an additional phone number? Type yes or no")
print("Saved phone number. Thank you for using this program!")

