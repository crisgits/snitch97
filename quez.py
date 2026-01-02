# 7. Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40
# marks =int(input("input student marks"))
# i=range(0,100)

    # Get user input for student marks
marks = float(input("Enter student marks (between 0 and 100): "))

    # Check if the input is within the valid range
if 0 <= marks <= 100:
        # Determine the grade based on the given marks
        if marks > 79:
            grade = 'A'
        elif 60 <= marks <= 79:
            grade = 'B'
        elif 50 <= marks <= 59:
            grade = 'C'
        elif 40 <= marks <= 49:
            grade = 'D'
        else:
            grade = 'E'

        print(f"The grade for {marks} is: {grade}")
else:
        print("Invalid input. Marks should be between 0 and 100.")

# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.

    # Get user input for the car's speed
speed = int(input("Enter the speed of the car: "))

speed_limit = 70
demerit_points=0
if speed <= speed_limit:
        print("Ok")
elif(speed>speed_limit and speed<75):
    demerit_points =1
else:
        demerit_points =round (speed - speed_limit) / 5

if demerit_points > 12:
            print("License suspended")
else:
            print(f"Points: {demerit_points}")
print(demerit_points)
            
#   9. Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....         

    # Get user input for the number of rows
rows = int(input("Enter the number of rows: "))

    # Check if the input is a positive integer
if rows > 0:
        # Loop to print the pattern of stars
        for i in range(1, rows + 1):
            print('  *' * i)
else:
        print("Please enter a positive integer.")
        
        
#  10.Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]
       
prods = [['omo', '30kshs', '300'], ['milk', '50kshs', '200'], ['bread', '45kshs', '359'], ['coffee', '5kshs', '79']]
total_stock = 0
for product in prods:
    stock = int(product[2][-1])
    
    total_stock += stock

print(f"The total stock in the company is: {total_stock}")

# 11.Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.
from datetime import datetime

try:
    # Get user input for date of birth
    dob_str = input("Enter your date of birth (YYYY-MM-DD): ")

    # Convert the input string to a datetime object
    dob = datetime.strptime(dob_str, "%Y-%m-%d")

    # Get the current date
    current_date = datetime.now()

    # Calculate the difference between the current date and date of birth
    age = current_date - dob

    # Calculate the number of years, months, and days
    years = age.days // 365
    remaining_days = age.days % 365
    months = remaining_days // 30
    days = remaining_days % 30

    # Print the age
    print(f"Your age is: {years} years, {months} months, and {days} days.")

except ValueError:
    print("Invalid input. Please enter your date of birth in the format YYYY-MM-DD.")

# 12.Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.
# Get user inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

largest_number = max(num1, num2, num3, num4)

print(f"The largest number is: {largest_number}")

# 14.Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
while True:
    
        input1 = input("Enter the first number: ")
        num1 = float(input1)
        input2 = input("Enter the second number: ")

        num2 = float(input2)

        result = num1 + num2

        print(f"The sum of {num1} and {num2} is: {result}")

        break

    # 15
basic_salary=int(input("Enter basic salary: "))
benefits=int(input("Enter basic benefits: "))



# 16
basic_salary = float (input("enter basic salary: "))
benefits = float(input("Enter benefits"))
gross_salary = basic_salary + benefits

rate = 0.06

if (gross_salary>0 and gross_salary<=18000):
    nsff=gross_salary*rate
else:
    nsff=18000*rate
    
    print(nsff)
    
    # 17
    NHDF=gross_salary * 0.015
    print(NHDF)
    
    # 18
    taxable_income=gross_salary-(nssf-NHDF)
    print(taxable_income)
    
    # 19
    relief =2400
    if taxable_income<= 24000:
        payee=(taxable_income * 0.1)-relief
    elif(taxable_income>24000 and taxable_income<=32333):
        payee((24000*0.1) + ((taxable_income-24000)*0.25))-relief
        
        print(payee)
        
        # 20
        net_salary = gross_salary - (nhif + NHDF + nssf + payee)
        
    