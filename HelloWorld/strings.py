# testing various examples with quotes

print('today is a good day to die')
print("your mother's watch")
print('test including "quotes" ')
print('string'+' concat')

greeting = "Hello"
name = "George"

print(greeting + ' ' + name)

age = 24
print(age)

# print variable type
print(type(greeting))
print(type(age))

age = "2 years" #  unlike JAVA and C we can change the variable type in Python
print(type(age))

# automatic type convertion won't work, like:
# print(name + 2)   >>> produces error

# what would work are f-strings:
age = 24
print(name + f" is {age} years old")

print(f"Pi is approx. {22 / 7 :12.50f}")
# or simpler:
pi = 22 / 7
print(f"Pi is approx {pi:12.50f}")