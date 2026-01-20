#!/usr/bin/env python
# coding: utf-8

# In[33]:


#this part of the code asks for the prices and number of people

childs_meal = float(input("What is the price of the child's meal?"))
adults_meal = float(input("What is the price of the adults's meal?"))
number_of_kids = int(input("How many children are there?"))
number_of_adults = int(input("How many adults are there?"))
print ()

#this part of the code calculates the subtotal before tax
childs_meal_total = childs_meal * number_of_kids   
adults_meal_total = adults_meal * number_of_adults
meal_subtotal = childs_meal_total + adults_meal_total 

print (f"Your subtotal before tax is: ${meal_subtotal:.2f}")
print()

#this part of the code calculates and shows the total 
tax_rate = float(input("Enter the tax amount: ")) #enter the tax amount as a percentage
sales_tax = float(meal_subtotal * tax_rate / 100) 

print (f"Sales Tax: ${sales_tax:.2f}")
total = sales_tax + meal_subtotal
print (f"${total:.2f}")
print()

#this part of the code asks the user if they want to tip, if yes, how much they will tip and that will be added to the total bill 
#.lower() changes the input to lowercase in the case that a user enters something different
add_tip = input("Would you like to add a tip? (yes/no): ").strip().lower() 
if add_tip == "yes": 
    tip = float(input("Enter the tip amount:"))
    bill = total + tip
else:
    print("That is not very nice of you")
    bill = total

print (f"Your total is: ${bill:.2f}")

#this part of the code calculates and shows the change
payment_amount = float(input("Enter the total cash offered: "))
change = float(payment_amount - bill)
print (f"Your change is: ${change:.2f}")
print ()


# In[ ]:




