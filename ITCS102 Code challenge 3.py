# Global Freight Calculator


sender_name = input("Enter sender name: ")
type_of_item = input("Enter type of item: ")
is_fragile = bool("Is the package fragile? ") 
weight = float(input("Enter weight (kg): "))
distance = float(input("Enter distance (km): "))
is_express = bool("Is it express?")
is_international = bool("Is it international?")


# Calculate Base Cost
base_cost = (weight * 2.50) + (distance * 0.15)


# Pricing Tiers
if weight <= 2.0 and distance <= 100 and is_express == false and is_international == false:
    total = 0.00

elif is_international  == trueand is_express == true:
    total = (base_cost * 1.40) + 50

elif is_express or (is_international and weight > 20):
    total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
    total = base_cost + 30

else:
    total = base_cost


print("Total shipping charge ->$",total)