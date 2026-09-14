#Temp conversion

celsius = float(input("Enter temperature in °C: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Celsius: {celsius} => Fahrenheit: {fahrenheit}")

#Silly name

Name = str(input("What is your name?"))
Adjective = str(input("Please provide an adjective."))
Verb = str(input("Please provide a verb(in past tense)."))
Place = str(input("Please provide a place."))

print(f"{Name} {Verb} to {Place} with a {Adjective} look on his face")

#Rectangle Calculation 

width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the the rectangle: "))
area = width * height
perimeter = 2 * (width + height)

print(f"The area of the given rectangle is {area:.3f}.\nThe perimeter of the given rectangle is {perimeter:.3f}.")

#