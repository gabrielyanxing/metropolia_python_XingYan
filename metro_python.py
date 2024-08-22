# 1.First program and deployment of version control
import math

print("Hello, Viivi Virta!")

# 2.Variables and interactive programs
# 2.1
name = input("What is your name? ")
print("Hello, " + name)

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

print("The weight in modern units: ")