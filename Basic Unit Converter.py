#length conversion functions  
def inches_to_feet(inches):
    return inches / 12

def feet_to_inches(feet):
    return feet * 12
# weight conversion functions
def pounds_to_ounces(pounds):
    return pounds * 16

def ounces_to_pounds(ounces):
    return ounces / 16

#temperature conversion functions

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
#main menu
print('Welcome to the Unit Converter! \n\nEnter a number:')
value = float(input())
conversion_type = input('\nWhich conversion would you like to perform?\n(inches, feet, pounds, ounces, fahrenheit, celsius): ')

#printing conversion
if conversion_type == 'inches':
    print(f"\n{value} inches is {inches_to_feet(value):.2f} feet.")
elif conversion_type == 'feet':
    print(f"\n{value} feet is {feet_to_inches(value):.2f} inches.")
elif conversion_type =='pounds':
    print(f"\n{value} pounds is {pounds_to_ounces(value):.2f} ounces.")
elif conversion_type =='ounces':
    print(f"\n{value} ounces is {ounces_to_pounds(value):.2f} pounds.")
elif conversion_type =='fahrenheit':
    print(f"\n{value} degrees Fahrenheit is {fahrenheit_to_celsius(value):.2f} degrees Celsius.")
elif conversion_type == 'celsius':
    print(f"\n{value} degrees celsius is {celsius_to_fahrenheit(value):.2f} degrees fahrenheit.")