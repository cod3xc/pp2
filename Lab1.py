# 1
print("Hello world!")

# 2
if 5 > 2:
    # This block runs because 5 is indeed greater than 2
    print("Five is greater than two!")


x = 5
y = "Hello world!"

print(x, y)


# 3
# This is an example of a single-line comment.
print("Hello, World!")


print("Hello, World!")  # A comment can also be placed at the end of a line.


print("Hello, World!")
# This is a comment that occupies its own line.

# You can write multi-line comments
# by starting each line
# with a hash symbol.
print("Hello, World!")


"""
Alternatively, for longer comments
spanning multiple lines, you can
use triple quotes like this.
"""
print("Hello, World!")

# 4 Variables

x = 5
y = "John"
print(x)
print(y)


x = 4        # Initially, x is an integer.
x = "Sally"  # Now, x has been reassigned to a string type.
print(x)

# You can specify the data type through casting.
x = str(3)    # x will be the string '3'
y = int(3)    # y will be the integer 3
z = float(3)  # z will be the float 3.0


x = 5
y = "John"
print(type(x))
print(type(y))


x = "John"
# This is the same as
x = 'John'


a = 4
A = "Sally"
# Note: 'A' will not overwrite 'a' because variable names are case-sensitive.


# 4 Variable Names


# Examples of legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Examples of illegal variable names:
# 2myvar = "sssss"  (Can't start with a number)
# my-var = "dsada"   (Can't use hyphens)
# my var = "sdasda"  (Can't include spaces)


# 4 Assigning Multiple Values

# Unpacking values into variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# Assigning the same value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)


# Unpacking a list into variables
fruits = [1, "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# 4 Outputting Variables

x = "Python is awesome"
print(x)


# The print function can output multiple variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


# You can also use the + operator to concatenate strings
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


# The + operator works as a mathematical addition for numbers
x = 5
y = 10
print(x + y)


# Printing different data types together
x = 5
y = "John"
print(x, y)

# 4 Global Variables

# 'x' is a global variable
x = "awesome"


def myfunc():
    # It can be accessed inside a function
    print("Python is " + x)


myfunc()

x = "awesome"


def myfunc():
    # This 'x' is a local variable, only existing within this function
    x = "fantastic"
    print("Python is " + x)


myfunc()

# The global 'x' remains unchanged
print("Python is " + x)


def myfunc():
    # The 'global' keyword modifies the global variable
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)


x = "awesome"


def myfunc():
    # Making 'x' global to change its value from within the function
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)


# 5 Numeric Types

x = 1      # integer
y = 2.8    # float
z = 1j     # complex number


print(type(x))
print(type(y))
print(type(z))

# Examples of integers
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Examples of floats
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Floats can also be scientific numbers with an "e"
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Examples of complex numbers
x = 3 + 5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


x = 1    # int
y = 2.8  # float
z = 1j   # complex

# Type Conversion
# from int to float:
a = float(x)

# from float to int (decimal part is removed):
b = int(y)

# from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# Importing the random module to generate a random number
import random

print(random.randrange(1, 10))

# String casting examples
x = str("s1")  # x becomes 's1'
y = str(2)     # y becomes '2'
z = str(3.0)   # z becomes '3.0'


# 6 Strings
# Multi-line strings can be created with triple quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Slicing a string to get a sub-string
b = "Hello, World!"
print(b[2:5])

# Slice from the start
b = "Hello, World!"
print(b[:5])

# Slice to the end
b = "Hello, World!"
print(b[2:])

# Negative indexing for slicing from the end
b = "Hello, World!"
print(b[-5:-2])

# Convert to uppercase
a = "Hello, World!"
print(a.upper())

# Convert to lowercase
a = "Hello, World!"
print(a.lower())

# Remove whitespace from the beginning or end
a = " Hello, World! "
print(a.strip())

# Replace a character or phrase
a = "Hello, World!"
print(a.replace("H", "J"))

# Split a string into a list
a = "Hello, World!"
print(a.split(","))

# String concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

# Concatenation with a space in between
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Using f-Strings to format strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)


price = 59
txt = f"The price is {price} dollars"
print(txt)

# F-strings with number formatting (2 decimal places)
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# You can also run expressions inside an f-string
txt = f"The price is {20 * 59} dollars"
print(txt)