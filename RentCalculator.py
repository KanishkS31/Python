#Rent Calculator calculates the rent of the flat given by per person on the bases of number of people living in the flat, food expenses, and electricity expenses.
# The rent is calculated by dividing the total rent by the number of people living in the flat and adding the food and electricity expenses to it.

persons = int(input("Enter the number of persons living in the hostel/flat = "))
rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the total amount of food ordered = "))
electricity_spent = int(input("Enter the total unit of electricity spent = "))
charge_per_unit = int(input("Enter the charge for electricity per unit = "))

total_bill = electricity_spent * charge_per_unit
output = (food + rent + total_bill) // persons

print("Each person will have to Pay = ", output)