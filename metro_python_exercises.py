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
    if max_num is None or number > max_num:
        max_num = number

    if min_num is None or number < min_num:
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

# 4.6
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

# 5.List structures and iterative loops (for)
# 5.1
the_number_of_dice_roll = input("Enter your numbers of dices:")
total_number = 0

for i in range(int(the_number_of_dice_roll)):
    random_number = random.randint(1, 6)
    print(random_number)
    total_number += random_number

print(total_number)

# 5.2
numbers_list = []
while True:
    number = input("Enter a number:")
    if number == "":
        break
    number = float(number)
    numbers_list.append(number)

numbers_list.sort(reverse=True)
print(numbers_list[:5])

# 5.3
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

# 5.4
city_name_list = []
for i in range(5):
    city_name = input("Enter a city name:")
    city_name_list.append(city_name)
for i in city_name_list:
    print(i)

# 6. Functions
# 6.1
def dice():
    random_dice = random.randint(1, 6)
    return random_dice

while True:
    dice_number = dice()
    print(f"The dice is {dice_number}.")
    if  dice_number == 6:
        break

# 6.2
def dice_sides(sides):
    random_dice_side = random.randint(1, sides)
    return random_dice_side

sides = int(input("Enter number of sides:"))

while True:
    random_dice_side = dice_sides(sides)
    print(f"The dice is {random_dice_side}.")
    if random_dice_side == sides:
        break

# 6.3
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

# 6.4
def int_list(user_list):
    sum_list = 0
    for i in user_list:
        sum_list += i
    return sum_list

mylist = [1,2,3,4,5,6,7]

print(f"The sum of the number in the list is {int_list(mylist)}.")

# 6.5
def int_list_b(user_list_b):
    for i in user_list_b:
        if i % 2 != 0:
            user_list_b.remove(i)
    return user_list_b

mylist_b = [1,2,3,4,5,6,7,8,9,10,11]
print(f"The original list is {mylist_b}.")
print(f"The cut-down list is {int_list_b(mylist_b)}.")

# 6.6
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

# 7 Tuple, set, and dictionary
# 7.1
season_tuple = ("spring", "spring", "spring",
                "summer", "summer", "summer",
                "autumn", "autumn", "autumn",
                "winter", "winter", "winter")
month_num = int(input("Enter a number of a month(1-12):"))
season = season_tuple[month_num-3]
print(season)

# 7.2
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


# 7.3
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

# 8. Using relational databases
# 8.1
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

# 8.2
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

# 8.3
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

# 9. Fundamentals of object-oriented programming
# 9.1 9.2 9.3 9.4
import random
class Car:

    def __init__(self, registration_number, maximum_speed, current_speed, travelled_distance):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += hours * self.current_speed

    def __str__(self):
        return (f"{self.registration_number}\t\t\t\t{self.maximum_speed} km/h\t"
                f"{self.current_speed} km/h\t\t\t{self.travelled_distance} km\t\t")

car1 = Car("ABC-123", 142, 0, 0)
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print(f"The current speed is {car1.current_speed} km/h.")

car1.accelerate(-200)
print(f"The current speed is {car1.current_speed} km/h.")

car2 = Car("ABC-123", 142, 60, 2000)
car2.drive(1.5)
print(f"The travelled distance is {car2.travelled_distance} km.")

car_list = [Car(f"ABC-{i+1}", random.randint(100, 200), 0, 0) for i in range(10)]

race_finished = False
while not race_finished:
    for x in car_list:
        x.accelerate(random.randint(-10, 15))
        x.drive(1)
        if x.travelled_distance >= 10000:
            race_finished = True

print("Registration Number\tMax Speed\tCurrent Speed\tTravelled Distance")
print("--------------------------------------------------------------")
for car3 in car_list:
    print(car3)

# 10. Association
# 10.1
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Elevator is at the top floor and cannot go up further.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Elevator is at the bottom floor and cannot go down further.")

    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            print("Invalid floor selection.")
            return

        while self.current_floor != floor:
            if self.current_floor < floor:
                self.floor_up()
            else:
                self.floor_down()


elevator = Elevator(1, 10)
print("Moving to floor 5")
elevator.go_to_floor(5)
print("Returning to ground floor")
elevator.go_to_floor(1)

# 10.2 10.3
class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(number_of_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"Running elevator {elevator_number} to floor {destination_floor}")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print("Invalid elevator number.")

    def fire_alarm(self):
        print("Fire alarm activated. Moving all elevators to the bottom floor.")
        for elevator2 in self.elevators:
            elevator2.go_to_floor(self.elevators[0].bottom_floor)


building = Building(1, 10, 3)
building.run_elevator(0, 5)
building.run_elevator(1, 8)
building.run_elevator(2, 3)
building.fire_alarm()

# 10.4
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"{self.name} Status:")
        for car in self.cars:
            print(f"{car}")

    def race_finish(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)


def Race_main():
    cars = [Car(f"ABC-{i+1}", random.randint(100, 200), 0, 0) for i in range(10)]
    race = Race("Grand Demolition Derby", 8000, cars)

    hours_passed = 0
    while not race.race_finish():
        race.hour_passes()
        hours_passed += 1
        if hours_passed % 10 == 0:
            race.print_status()

    race.print_status()
    print(f"Race finished in {hours_passed} hours.")

Race_main()

# 11. Inheritance
# 11.1
class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book Name: {self.name}\nAuthor: {self.author}\nPage Count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine Name: {self.name}\nChief Editor: {self.chief_editor}")


donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
compartment_no_6 = Book("Compartment No.6", "Rosa Liksom", "192")


donald_duck.print_information()
compartment_no_6.print_information()

# 11.2
class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed, current_speed=0, travelled_distance=0)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed, current_speed=0, travelled_distance=0)
        self.tank_volume = tank_volume


electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(150)
gasoline_car.accelerate(120)

electric_car.drive(3)
gasoline_car.drive(3)

print("_____________________________________________________________")
print("Vehicle Information:")
print("Registration\t\tMax Speed\tCurrent Speed\tTravelled Distance")
print(electric_car)
print(gasoline_car)

# 12. Using external interfaces
# 12.1
import requests
def fetch_random_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"

    response = requests.get(url)
    joke_data = response.json()

    joke_text = joke_data.get("value", "Not found")
    return joke_text


joke = fetch_random_chuck_norris_joke()
print(joke)

# 12.2
def city():

    city_name = input("Enter a city name:")
    country_code = input("You can type in the country code to remove ambiguity, or you can hit enter to skip it.\n"
                         "Enter the country code:")
    api_key = "3462ee9cb0e2472d831723f1deabd315"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}"

    response = requests.get(url)

    if response .status_code == 200:
        data = response.json()
        weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        print(f"{'City Name':<15} {'Weather Condition':<20} {'Weather Description':<20} {'Celsius Degrees':<15}")
        print(f"{city_name:<15} {weather:<20} {description:<20} {temperature_celsius:15.1f}")

    else:
        print("Error:", response.status_code)

city()