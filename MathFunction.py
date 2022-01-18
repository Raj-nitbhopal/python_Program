# import math
# print("CONSTANTS IN PYTHON")
# print(" PI value : ", math.pi)
# print(" E value : ", math.e)
# print(" nan value : ", math.nan)
# print(" E value : ", math.inf)
# print((math.log10(100)))
# print(math.exp(1))
# print(math.expm1(1))
# print(math.pow(4, 5))
# print(math.sqrt(16))

# def sub(a, b):
#     s = a - b
#     return s
#
#
# def mult(a, b):
#     s = a * b
#     return s
# x = 12
# y = 5
# r = sub(x, y)
# rs = mult(x, y)
# print(r)
# print(rs)
#
#
# def mult(a, b):
#     s = a * b
#     return s
# print(mult("Ram", 2))

class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# create a new object of Person class
harry = Person()

# Output: <function Person.greet>
print(Person.greet)

# Output: <bound method Person.greet of <__main__.Person object>>
print(harry.greet)

# Calling object's greet() method
# Output: Hello
harry.greet()