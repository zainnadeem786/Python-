print("Hello World")
# Using Variables in Python
message = "Hello_World"
print(message)
message = "Hello Python Crash Course World"
print(message)
# NameError in Python
message = "Hi Dear"
print(message)
# Methods in Python (Changing Case)
hello = "my name is zain"
print(hello.title())
# Using Variables in String
first_name = "Zain"
last_name = "Nadeem"
print(f"{first_name} {last_name}")
print(f"Hello!{first_name.title()}")

# Modifying list
cars = ['Honda', 'Toyota','Kia']
print(cars)
cars.append('BMW')
print(cars)
# Sorting list
cars.sort()
print(cars)
# Find the lenght of list
len(cars)
# For loop in List
py_students = ['zain','ahmad','osama','ashad','sarim']
for py_std in py_students:
    print(f'{py_std.title()}, is a Python Programer')
# Range Function
for value in range(1,9):
    print(value)
# Tuple in python
# std = ('Zain', 'Ashad')
# print(std[1])
# std[0] = 'Ali'
# if Statement
car = ['Honda','toyota','bmw']
for cars in car:
    if cars == 'bmw':
     print(cars.upper())
    else:
        print(cars.title())
