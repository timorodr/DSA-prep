# name = input('What is your name: ? ')
# age = input('What is your age: ? ')

# print("Hello " + name + ' You are ' + age + '!')

# num1 = input("Enter a digit: ")
# num2 = input("Enter a second number: ")
# #convert strings to number
# answer = float(num1) + float(num2)
# print(answer)


# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

name = input("What is your name?: ")
km = input("Distance in km?: ")
miles = float(km) / 1.609

print(f'Hello {name.capitalize()} the km is {km} and miles are {round(miles, 1)}')