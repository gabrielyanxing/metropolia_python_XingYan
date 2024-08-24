![Metropolia](https://cookie-cdn.cookiepro.com/logos/4167d0b9-598c-4c19-adcb-dbf31e3c74f0/18d85870-9dc6-4362-a7b0-3772a78cc17f/a4fd611e-5ca6-427b-a86d-f6bd35128c2d/metropolia_logo.png)
# Metropolia-Python-Exercises 
#### Group B: XING YAN
[Python File Link](https://github.com/gabrielyanxing/metropolia_python_XingYan/blob/main/metro_python_exercises.py)
***
## 1. First program and deployment of version control
### 1.1
```python
print("Hello, Viivi Virta!")
```
***
## 2. Variables and interactive programs
### 2.1
```python
name = input("What is your name?\n")  
print(f"Hello, {name}.")
```

### 2.2
```python
import math
radius = float(input("Enter a radius: "))  
the_area_of_circle = math.pi * radius**2  
print("The area is %.2f." % the_area_of_circle)
```

### 2.3
```python
length = float(input("Enter a length: "))  
width = float(input("Enter a width: "))  
the_perimeter_of_rectangle = (length + width) * 2  
the_area_of_rectangle = length * width  
print("The perimeter is %.2f." % the_perimeter_of_rectangle)  
print("The area is %.2f." % the_area_of_rectangle)
```
### 2.4
```python
first_integer_number = int(input("Enter a integer: "))  
second_integer_number = int(input("Enter a integer: "))  
third_integer_number = int(input("Enter a integer: "))  
the_sum = first_integer_number + second_integer_number + third_integer_number  
the_product = first_integer_number * second_integer_number * third_integer_number  
the_average = the_sum / 3  
print(f"The sum is {the_sum}.")  
print(f"The product is {the_product}.")  
print("The average is %.2f." % the_average)
```
### 2.5
```python
talents = float(input("Enter talents: "))  
pounds = float(input("Enter pounds: "))  
lots = float(input("Enter lots: "))  
grams = talents*20*32*13.3+pounds*32*13.3+lots*13.3  
kilograms = grams//1000  
remainder = grams%1000  
print("The weight in modern unit:")  
print("%.0f kilograms and %.2f grams." %(kilograms,remainder))  
```  
### 2.6
```python
import random
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
```
***
## 3. Conditional structures (if)
### 3.1
```python
length = float(input("Enter the length of a zander in centimeters:"))  
if length < 42:  
    print("%.1f centimeters below the size limit the caught fish was.And release the fish back into the lake." % (42-length))  
else:  
    print("the zander does fulfill the size limit.")
```
### 3.2
```python
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
```
### 3.3
```python
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
```
### 3.4
```python
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
```
