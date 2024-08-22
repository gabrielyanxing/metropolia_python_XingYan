a = 2
b = 1
print("a is: ", a)
print("b is: ", b)
user_input = int(input("Enter a number: "))
if user_input == a:
    print(b)
elif user_input == b:
    print(a)

width = float(input("Enter a width: "))
length = float(input("Enter a length: "))
area = width * length
perimeter = 2 * (length + width)
print("Area is: ", area)
print("Perimeter is: ", perimeter)

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
grams = talents*20*32*13.3+pounds*32*13.3+lots*13.3
kilograms = grams//1000
remainder = grams%1000
print("The weight in modern unit:")
print("%.0f kilograms and %.2f grams." %(kilograms,remainder))