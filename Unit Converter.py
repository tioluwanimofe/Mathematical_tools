# Code to look for the specific units in whatever text is inputted so that the program would run
# whatever code assigned to that unit
print("This is a product of BOTS of tommorrow, which is solely owned by Adesanya Tioluwanimofe." \n " Do ensure to endorse the code. Thank you")
print("Please first enter the unit to be converted from then enter the unit to be converted to")
print("Use \n cm- Centimeter \n m- Meter \n c- Celsius \n f- Fahrenheit \n d- USD dollar \n n- Naira")

Unit1 = input("Enter the first unit: ")
Unit2 = input("Enter the second unit: ")


# Function for celsius to fahrenheit
def temperature():
    celsius = int(input())
    f = 9 / 5
    a = f * celsius
    h = a + 32
    print(h)


def temperature1():
    fahrenheit = int(input())
    c = fahrenheit - 32
    e = c * 5
    s = e / 9
    print(s)


# For updated version, pip a currency library that will continuously import the current currency value
def currency():
    naira = int(input())
    d = 415.87
    o = naira / d
    print(o)


def currency1():
    dollar = int(input())
    n = 415.87
    o = dollar * n
    print(o)


def length1():
    meter = int(input())
    c = 100
    e = meter / c
    print(e)


def length():
    centimeter = int(input())
    m = 100
    e = centimeter * m
    print(e)


# Algorithm to check for the option picked
if Unit1 == "c" and Unit2 == "f":
    temperature()
elif Unit1 == "f" and Unit2 == "c":
    temperature1()
elif Unit1 == "cm" and Unit2 == "m":
    length1()
elif Unit1 == "m" and Unit2 == "cm":
    length()
elif Unit1 == "d" and Unit2 == "m":
    currency1()
elif Unit1 == "n" and Unit2 == "d":
    currency()
