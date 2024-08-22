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
