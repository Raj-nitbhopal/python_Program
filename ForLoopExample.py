#! /usr/bin/python
greeting = 'Hello Python'
# here we are taking for loop
for letter in greeting:
    print(letter)

print('\n----------------------------')

color = ["green", "pink", "red"]
for c in color:
    print(c)
    if c == "pink":
        break
print('\n----------------------------')

for letter in 'Hello John':
    print('current letter :', letter)

print('\n----------------------------')

for r in range(1, 5, 1):
    print(r)

print('\n----------------------------')

cars = ['toyota', 'tata', 'honda']
for car in range(len(cars)):
    print("current car:", cars[car])

print('\n----------------------------')

no = [1, 2]
color = ["red", "blue"]
for x in no:
    for y in color:
        print(x, y)

print('\n----------------------------')
print("Enter Number:")
n = int(input())
for i in range(1, 10):
    print(str(n) + " X " + str(i) + ' = ' + str(i * n))

for i in range(1, n):
    for j in range(1, n):
        print('*', end='')
    print('')