import math
import random

# 1.First program and deployment of version control
print("Hello, Viivi Virta!")

# 2.Variables and interactive programs
# 2.1
name = input("What is your name?: ")
print("Hello, " + name + ".")

# 2.2
radius = float(input("Enter a radius: "))
the_area_of_circle = math.pi * radius**2
print("The area is " + str(the_area_of_circle) + ".")

# 2.3
length = float(input("Enter a length: "))
width = float(input("Enter a width: "))
the_perimeter_of_rectangle = (length + width) * 2
the_area_of_rectangle = length * width
print("The perimeter is " + str(the_perimeter_of_rectangle) + ".")
print("The area is " + str(the_area_of_rectangle) + ".")

# 2.4
first_integer_number = int(input("Enter a integer: "))
second_integer_number = int(input("Enter a integer: "))
third_integer_number = int(input("Enter a integer: "))
the_sum = first_integer_number + second_integer_number + third_integer_number
the_product = first_integer_number * second_integer_number * third_integer_number
the_average = the_sum / 3
print("The sum is " + str(the_sum) + ".")
print("The product is " + str(the_product) + ".")
print("The average is " + str(the_average) + ".")

# 2.5
talents = int(input("Enter talents: "))
pounds = int(input("Enter pounds: "))
lots = int(input("Enter lots: "))
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

num4 = random.randint(1,6)
num5 = random.randint(1,6)
num6 = random.randint(1,6)
print(num4,num5,num6)

# 3.Conditional structures(if)
# 3.1
length = float(input("Enter the length of a zander in centimeters:"))
if length < 42:
    print("%.1f centimeters below the size limit the caught fish was.And release the fish back into the lake." % (42-length))
else:
    print("the zander does fulfill the size limit")

# 3.2
cabin_class = input("Enter the cabin calss of a curise ship(LUX,A,B,C):")
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
biological_gender = input("Enter your biological_gender:")
hemoglobin_value = float(input("Enter your hemoglobin value (g/l):"))
if biological_gender == "female":
    if hemoglobin_value >= 117 and hemoglobin_value <= 155:
        print("Yuor hemoglobin value is normal!")
    else:
        print("Yuor hemoglobin value is not normal!")
elif biological_gender == "male":
    if hemoglobin_value >= 134 and hemoglobin_value <= 167:
        print("Yuor hemoglobin value is normal!")
    else:
        print("Yuor hemoglobin value is not normal!")

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