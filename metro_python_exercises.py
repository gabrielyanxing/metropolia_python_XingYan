import math
import random

# 1.First program and deployment of version control
print("Hello, Viivi Virta!")

# 2.Variables and interactive programs
# 2.1
name = input("What is your name?\n")
print(f"Hello, {name}.")

# 2.2
radius = float(input("Enter a radius: "))
the_area_of_circle = math.pi * radius**2
print("The area is %.2f." % the_area_of_circle)

# 2.3
length = float(input("Enter a length: "))
width = float(input("Enter a width: "))
the_perimeter_of_rectangle = (length + width) * 2
the_area_of_rectangle = length * width
print("The perimeter is %.2f." % the_perimeter_of_rectangle)
print("The area is %.2f." % the_area_of_rectangle)

# 2.4
first_integer_number = int(input("Enter a integer: "))
second_integer_number = int(input("Enter a integer: "))
third_integer_number = int(input("Enter a integer: "))
the_sum = first_integer_number + second_integer_number + third_integer_number
the_product = first_integer_number * second_integer_number * third_integer_number
the_average = the_sum / 3
print(f"The sum is {the_sum}.")
print(f"The product is {the_product}.")
print("The average is %.2f." % the_average)

# 2.5
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
grams = talents*20*32*13.3+pounds*32*13.3+lots*13.3
kilograms = grams//1000
remainder = grams%1000
print("The weight in modern unit:")
print("%.0f kilograms and %.2f grams." %(kilograms,remainder))

# 2.6
num1 = random.randint(0,9)
num2 = random.randint(0,9)
num3 = random.randint(0,9)
print(num1,num2,num3)
num4 = random.randint(0,9)
num5 = random.randint(0,9)
num6 = random.randint(0,9)
print(num4,num5,num6)

num7 = random.randint(1,6)
num8 = random.randint(1,6)
num9 = random.randint(1,6)
num10 = random.randint(1,6)
print(num7,num8,num9,num10)
num11 = random.randint(1,6)
num12 = random.randint(1,6)
num13 = random.randint(1,6)
num14 = random.randint(1,6)
print(num11,num12,num13,num14,num11)

# 3.Conditional structures(if)
# 3.1
length = float(input("Enter the length of a zander in centimeters:"))
if length < 42:
    print("%.1f centimeters below the size limit the caught fish was.And release the fish back into the lake." % (42-length))
else:
    print("The zander does fulfill the size limit.")

# 3.2
cabin_class = input("Enter the cabin class of a cruise ship(LUX,A,B,C):")
if cabin_class == "LUX":
    print("LUX:upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("A:above the car deck,equipped with a window.")
elif cabin_class == "B":
    print("B:windowless cabin above the car deck.")
elif cabin_class == "C":
    print("C:windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

# 3.3
biological_gender = input("Enter your biological_gender(female/male):")
hemoglobin_value = float(input("Enter your hemoglobin value (g/l):"))
if biological_gender == "female":
    if hemoglobin_value < 117:
        print("Your hemoglobin is LOW!")
    elif hemoglobin_value > 155:
        print("Your hemoglobin is HIGH!")
    else:
        print("Your hemoglobin value is normal!")
elif biological_gender == "male":
    if hemoglobin_value < 134:
        print("Your hemoglobin is LOW!")
    elif hemoglobin_value > 167:
        print("Your hemoglobin is HIGH!")
    else:
        print("Your hemoglobin value is normal!")

# 3.4
year = int(input("Enter a year:"))
if (year % 4) == 0:
    if (year % 100) != 0:
        if (year % 400) == 0:
            print("It's a leap year.")
        else:
            print("It's not a leap year.")
    else:
        print("It's a leap year.")
else:
    print("It's not a leap year.")

# 4.While loops(while)
# 4.1
i = 0
while i <= 1000:
    print(i)
    i += 3

# 4.2
inches = float(input("Enter inches: "))
while inches >= 0:
    centimeters  = inches * 2.54
    print(f"{inches} inches is {centimeters} centimeters")
    inches = float(input("Enter inches: "))
print("Please enter a positive number!")

# 4.3
max_num = None
min_num = None
while True:
    number = input("Enter a number: ")
    if number == "":
        print("Bye!")
        break

    number = float(number)
    if max_num is None or max_num > number:
        max_num = number

    if min_num is None or min_num < number:
        min_num = number

if (max_num and min_num) is not None:
    print(f"The max number is {max_num},the min number is {min_num}.")

# 4.4
import random
random_num = random.randint(1,10)
while True:
    guess_num = int(input("Enter the number you guessed:"))
    if guess_num == random_num:
        print("Correct!")
        break
    else:
        if guess_num > random_num:
            print("Too,high!")
        else:
            print("Too,low!")

# 4.5
username = "root"
password = "123456"
count = 0
while True:
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    count += 1
    if username_input == username and password_input == password:
        print("Welcome")
        break
    elif username_input != username or password_input != password:
        print("invalid input, enter again")
        if count == 4:
            print("Access denied")
            break

# 4.6
