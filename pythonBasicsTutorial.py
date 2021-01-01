# In this Tutorial, you will be learning Python Basics

# What is Python?
#  - Python is an interpreted, high-level and general-purpose programming language.
#  - Python's design philosophy emphasizes code readability with its notable use of significant whitespace.

# Uses Of Python?
#  - Used for making Scalable Web Applications using its frameworks like Flask, Django, e.t.c.
#  - Used for the development of GUI (Graphical User Interface) using its frameworks like Tkinter, e.t.c.
#  - Used for making games using its frameworks like PyGame, e.t.c.
#  - And much more uses...

#################### So, lets start the Python Programming ####################

# 1. How to print something in console or terminal using Python?
#  - For this we have to use a function provided by python which is print().
import math
print("hello world")
# Output: hello world

# 2. Modules in Python:
#  - Modules are set the of codes written for the ease of us.
#  - Modules are of Two Types 1. Internal Modules Or Built-In Modules 2. External Modules
#  - To install An External Module we have to write this command in our terminal, pip install moduleName.
#  - So, in this tutorial, i shall be importing the Built-In Module of python.
#  - So, I have imported math module let me use it!
print(math.floor(98.729))
#  - math.floor(value) is a function which accepts a value in its parameter and gives us the floor of it.
# Output: 98

# 3. Comments in Python:
#  - Comments are something which are not executed by Python Interpreter and are written by (#).

# 4. Variables in Python:
#  - Variables stores values of specific data-type in them.
#  - Making variables:
num1 = 50
num2 = 70
print("The Sum Of", num1, "and", num2, "is" + ":", num1 + num1)
# Output: The Sum Of 50 and 70 is: 100
percentage = 97.78
print(percentage)
# Output: 97.78
bioData = "My name is Abdullah Sajjad. I am a Python and Flask Web Developer"
print(bioData)
# Output: My name is Abdullah Sajjad. I am a Python and Flask Web Developer
# Check Type of any varibale
print(type(bioData))
# Output: <class 'str'>

# 5. String Functions in Python:
str1 = "this is a string stored in variable str1"
# Function to capitalize the first letter of the first word of the string:
print(str1.capitalize())
# Output: This is a string stored in variable str1
# Function to find particular sub-strings in a string:
# It tell the index on which that sub-string starts and if not present then it tells, -1
print(str1.find("stored"))
# Output: 17
# Function to CAPITALIZE all the letters in the string:
print(str1.upper())
# Output: THIS IS A STRING STORED IN VARIABLE STR1
# Function to lower all the letters in the string:
print(str1.lower())
# Output: this is a string stored in variable str1

# 6. Lists in Python:
#  - Lists are mutable
listOfRandomThings = ["Apple", 28, "Laptop", "School", 87]
print("At Index 2:", listOfRandomThings[2])
# Output: At Index 2: Laptop
# Adding a value to the list
listOfRandomThings.append("Asus")
print(listOfRandomThings)
# Output: ['Apple', 28, 'Laptop', 'School', 87, 'Asus']

# 7. Tuple in Python:
#  - Tuple are immutable (whose values cannot be changed)
tupleOfRandomThings = ("Chrome", "MacBook", 90, "Horse")
print(tupleOfRandomThings[1])
# Output: MacBook

# 8. Dictionary in Python:
#  - Dictionaries are the set of key value pairs
studentWithIds = {
    "Abdullah Sajjad": 2727,
    "Nouman Kamran": 2134,
    "Abu Bakar": 2192
}
print(studentWithIds)
# Output: {'Abdullah Sajjad': 2727, 'Nouman Kamran': 2134, 'Abu Bakar': 2192}
print(studentWithIds["Abdullah Sajjad"])
# Output: 2727
print(studentWithIds.get("Abu Bakar"))
# Output: 2192
# Adding a new key with value
studentWithIds["Moazzam"] = 1486
# Gettings Items
print(studentWithIds.items())
# Output: dict_items([('Abdullah Sajjad', 2727), ('Nouman Kamran', 2134), ('Abu Bakar', 2192), ('Moazzam', 1486)])
# Getting Keys
print(studentWithIds.keys())
# Output: dict_keys(['Abdullah Sajjad', 'Nouman Kamran', 'Abu Bakar', 'Moazzam'])
# Getting Values
print(studentWithIds.values())
# Output: dict_values([2727, 2134, 2192, 1486])

# 9. Set in Python:
#  - Set is a data-structure in python in which a same value cannot be repeat
set1 = {"Abdullah", 87, 65, "Huawei"}
print(set1)
# Output: {65, 'Huawei', 87, 'Abdullah'}

# 10. Type-Casting in Python:
num = 965
numToStr = str(num)
print("The Type Of", num, "is", type(num), "& The Type Of",
      numToStr, "after conversion is", type(numToStr))
# Output: The Type Of 965 is <class 'int'> & The Type Of 965 after conversion is <class 'str'>

# 11. Basic Operators in Python:
#  (+) for addition
#  (-) for subtraction
#  (*) for multiplication
#  (/) for division
#  (%) for modules (remainder)

# 11. Getting Input from user by input() function:
userName = str(input("Enter Your Name: "))
print("User Name is " + userName)

# 12. if-else-elif in Python:
# if-else-elif are conditional statements
age = int(input("Enter Your Age: "))
if (age >= 18 and age <= 70):
    print("You are allowed to drive!!!")
elif (age < 17):
    print("You are not allowed to drive because you are underage!!!")
else:
    print("You are not allowed to drive!!!")

# 13. Loops in Python:
#  - For-Loop in Python:
for i in range(0, 101):
    print("Number Of For-Loop:", i)

#  - While-Loop in Python:
numForWhile = 0
while (numForWhile <= 100):
    print("Number Of While-Loop:", numForWhile)
    numForWhile = numForWhile + 1

# 14. Functions in Python:


def average(num1, num2):
    avr = (num1 + num2) / 2
    return float(avr)


print(average(20, 10))

# 15. Exception Handling in Python:
try:
    whatAge = int(input("Enter Your Age: "))
    print(whatAge)
except Exception as e:
    print("Write Only Integer!")

# 16. File-Handling in Python:
f = open("bioData.txt", "w")
f.write("My name is Abdullah Sajjad")
f.close()
fNew = open("bioData.txt", "r")
contentOfFile = fNew.read()
print(contentOfFile)
# Output: My name is Abdullah Sajjad

#################### Python Basics Tutorial Completed ####################
