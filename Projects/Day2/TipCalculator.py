# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator.")
bill_to_pay = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
n_people_to_pay = input("How many people to split the bill? ")

split_bill = round((float(bill_to_pay) / int(n_people_to_pay)) * (1 + int(tip) / 100), 2)

print(f"Each person should pay: ${split_bill}")
