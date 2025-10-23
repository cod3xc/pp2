#1
import functools, operator
list = [ 1, 2, 3, 4, 5, 6]
print(functools.reduce(operator.mul, list))


#2
string = 'KJdnkcajkJCAjkcnasc JKCnalknsaknca Jjjasjacoqwporiojknnc'
print(f"Uppers: {sum(1 for i in string if i.isupper())}\nLowers: {sum(1 for i in string if i.islower())}")


#3
string = "teacher"
print(f"Polindrome: {string == string[::-1]}")


#4
import time, math

input, delay = 25100, 2123

time.sleep(delay / 1000)
print(f"Square root of {input} after {delay} miliseconds is {math.sqrt(input)}")


#5
tuple_1, tuple_2 = (True, 1, "Str"), (False, 1, "Str")
print(all(tuple_1))
print(all(tuple_2))