![Metropolia](https://cookie-cdn.cookiepro.com/logos/4167d0b9-598c-4c19-adcb-dbf31e3c74f0/18d85870-9dc6-4362-a7b0-3772a78cc17f/a4fd611e-5ca6-427b-a86d-f6bd35128c2d/metropolia_logo.png)
# Metropolia-Python-Exercises 
#### Group B: XING YAN
---> [Python File Link](https://github.com/gabrielyanxing/metropolia_python_XingYan/blob/main/metro_python_exercises.py)
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
    print("The zander does fulfill the size limit.")
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
## 4. While loops(while)
### 4.1
```python
i = 0
while i <= 1000:
    print(i)
    i += 3
```
### 4.2
```python
inches = float(input("Enter inches: "))
while inches >= 0:
    centimeters  = inches * 2.54
    print(f"{inches} inches is {centimeters} centimeters")
    inches = float(input("Enter inches: "))
print("Please enter a positive number!")
```
### 4.3
```python
max_num = None
min_num = None
while True:
    number = input("Enter a number: ")
    if number == "":
        print("Bye!")
        break

    number = float(number)
    if max_num is None or number > max_num:
        max_num = number

    if min_num is None or number < min_num:
        min_num = number

if (max_num and min_num) is not None:
    print(f"The max number is {max_num},the min number is {min_num}.")
```
### 4.4
```python
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
```
### 4.5
```python
username = "python"
password = "password"
counter = 0
while True:
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    counter += 1
    if username_input == username and password_input == password:
        print("Welcome")
        break
    elif username_input != username or password_input != password:
        print("invalid input, enter again")
        if counter == 5:
            print("Access denied")
            break
```
### 4.6
```python
import random
count_xy = 0
count_circle_points = 0
user_points = int(input("Enter number of points: "))
while True:
    num_x = random.uniform(-1, 1)
    num_y = random.uniform(-1, 1)
    count_xy += 1

    if num_x ** 2 + num_y ** 2 < 1:
        count_circle_points += 1

    approximation = (4 * count_circle_points) / user_points

    if count_xy == user_points:
        break

print(f"The approximation is {approximation}.")
```
## 5. List structures and iterative loops (for)
### 5.1
```python
import random
the_number_of_dice_roll = input("Enter your numbers of dices:")
total_number = 0

for i in range(int(the_number_of_dice_roll)):
    random_number = random.randint(1, 6)
    print(random_number)
    total_number += random_number

print(total_number)
```
### 5.2
```python
numbers_list = []
while True:
    number = input("Enter a number:")
    if number == "":
        break
    number = float(number)
    numbers_list.append(number)

numbers_list.sort(reverse=True)
print(numbers_list[:5])
```
### 5.3
```python
number_user_input = int(input("Enter a number:"))

if number_user_input > 1:
    for i in range(2, number_user_input):
        if number_user_input % i == 0:
            print("The number is not a prime number.")
            break
    else:
        print("The number is a prime number.")
else:
    print("The number is not a prime number.")
```
### 5.4
```python
city_name_list = []
for i in range(5):
    city_name = input("Enter a city name:")
    city_name_list.append(city_name)
for i in city_name_list:
    print(i)
```
## 6. Functions
### 6.1
```python
import random
def dice():
    random_dice = random.randint(1, 6)
    return random_dice

while True:
    dice_number = dice()
    print(f"The dice is {dice_number}.")
    if  dice_number == 6:
        break
```
### 6.2
```python
import random
def dice_sides(sides):
    random_dice_side = random.randint(1, sides)
    return random_dice_side

sides = int(input("Enter number of sides:"))

while True:
    random_dice_side = dice_sides(sides)
    print(f"The dice is {random_dice_side}.")
    if random_dice_side == sides:
        break
```
### 6.3
```python
def us_gal_l(us_gal):
    litre = 0.264172052358 * us_gal
    return litre

while True:
    us_gal = float(input("Enter your US gal value:"))
    output_litre = us_gal_l(us_gal)
    if us_gal < 0:
        print("Exit")
        break
    print(f"{us_gal} = {output_litre:.2f}")
```
### 6.4
```python
def int_list(user_list):
    sum_list = 0
    for i in user_list:
        sum_list += i
    return sum_list

mylist = [1,2,3,4,5,6,7]

print(f"The sum of the number in the list is {int_list(mylist)}.")
```
### 6.5
```python
def int_list_b(user_list_b):
    for i in user_list_b:
        if i % 2 != 0:
            user_list_b.remove(i)
    return user_list_b

mylist_b = [1,2,3,4,5,6,7,8,9,10,11]
print(f"The original list is {mylist_b}.")
print(f"The cut-down list is {int_list_b(mylist_b)}.")
```
### 6.6
```python
import math
def pizza(diameter,price):
    radius_in_meters = (diameter / 2) / 100
    the_area_of_pizza = math.pi * radius_in_meters ** 2
    price_per_square_meter = price / the_area_of_pizza
    return price_per_square_meter

pizza_a_diameter = float(input("Enter the first pizza diameter:"))
pizza_a_price = float(input("Enter the first pizza price:"))
pizza_b_diameter = float(input("Enter the second pizza diameter:"))
pizza_b_price = float(input("Enter the second pizza price:"))

if pizza(pizza_a_diameter,pizza_a_price) < pizza(pizza_b_diameter,pizza_b_price):
    print("The first pizza is a better deal.")
elif pizza(pizza_a_diameter,pizza_a_price) > pizza(pizza_b_diameter,pizza_b_price):
    print("The second pizza is a better deal.")
else:
    print("Both pizzas offer the same value.")
```
## 7. Tuple, set, and dictionary
### 7.1
```python
season_tuple = ("spring", "spring", "spring",
                "summer", "summer", "summer",
                "autumn", "autumn", "autumn",
                "winter", "winter", "winter")
month_num = int(input("Enter a number of a month(1-12):"))
season = season_tuple[month_num-3]
print(season)
```
### 7.2
```python
name_set = set()
while True:
    name = input("Enter a name:")

    if name == "":
        break

    elif name in name_set:
        print("Existing name!")

    else:
        print("New name!")
    name_set.add(name)

for name in name_set:
    print(name)
```
### 7.3
```python
airport = {"EFHK":"Helsinki-Vantaa Airport"}
while True:
    start_ask = input("Choose an option:Enter a new airport[E] "
                      "Fetch the information of an existing airport[F] "
                      "Quit[Q]:").upper()

    if start_ask == "E":
        icao = input("Enter the airport's ICAO code:").upper()
        if icao in airport:
            print("This ICAO code already exists in the database.")
        else:
            airport_name = input("Enter the airport name:")
            airport[icao] = airport_name
            print(f"{airport_name} and {icao} code have been added to the database.")

    elif start_ask == "F":
        icao = input("Enter the ICAO code of the airport you want to fetch: ").upper()
        airport_name = airport.get(icao)
        if airport_name:
            print(f"The airport name for ICAO code '{icao}' is '{airport_name}'.")
        else:
            print("I can't found the airport name with that ICAO code in the database.")

    elif start_ask == 'Q':
        print("Exiting the program.")
        break
```
## 8. Using relational databases
### 8.1
```python
import mysql.connector
def connect_to_mariadb_city():
    conn = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        database = 'Airport',
        user = 'root',
        password = '123456',
        autocommit = True
    )
    return conn
def get_airport_location_city(icao, conn):
    cursor = conn.cursor()
    query = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(query, (icao,))
    result = cursor.fetchone()
    cursor.close()
    return result if result else None

icao_input = input("Enter your ICAO:").upper()
conn = connect_to_mariadb_city()
airport_city = get_airport_location_city(icao_input, conn)

if airport_city:
    print(f"The name of airport is {airport_city[0]}, in {airport_city[1]}.")
else:
    print("Invalid isao code.")

conn.close()
```
### 8.2
```python
import mysql.connector
def connect_to_mariadb():
    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='Airport',
        user='root',
        password='123456',
        autocommit=True
    )
    return conn

def get_airports_by_country(iso_country, conn):
    cursor = conn.cursor()
    query = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type ORDER BY type"
    cursor.execute(query, (iso_country,))
    result = cursor.fetchall()
    cursor.close()
    return result

iso_country_input = input("Enter the country code (for example 'FI' for Finland): ").upper()

conn = connect_to_mariadb()
airports = get_airports_by_country(iso_country_input, conn)

if airports:
    print(f"Airports in {iso_country_input} by type:")
    for airport_type, count in airports:
        print(f"{airport_type}: {count}")
else:
    print(f"No airports found for the country code: {iso_country_input}")

conn.close()
```
### 8.3
```python
import mysql.connector
from geopy.distance import geodesic

def connect_to_mariadb():
    conn = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='Airport',
        user='root',
        password='123456',
        autocommit=True
    )
    return conn


def get_airport_location(icao, conn):
    cursor = conn.cursor()
    query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(query, (icao,))
    result = cursor.fetchone()
    cursor.close()
    return result


def calculate_distance(icao1, icao2, conn):
    loc1 = get_airport_location(icao1, conn)
    loc2 = get_airport_location(icao2, conn)
    print(loc1)
    if loc1 and loc2:
        distance = geodesic(loc1, loc2).kilometers
        return distance
    else:
        return None


def main():
    icao1 = input("Enter the first ICAO code: ")
    icao2 = input("Enter the second ICAO code: ")

    conn = connect_to_mariadb()
    distance = calculate_distance(icao1, icao2, conn)
    if distance is not None:
        print(f"The distance between {icao1} and {icao2} is {distance:.2f} kilometers.")
    else:
        print("Could not find one or both airports.")

    conn.close()
    
if __name__ == '__main__':
    main()
```