num1 = 4
num2 = 8
if(num1 < num2):
   print("1.Inside if condition")

num1 = 4
num2 = 8
if(num1 > num2):
   print("2.Inside if condition")

num1 = 1
num2 = 0
if(num1):
   print("3.Inside if condition")

num1 = 1
num2 = 0
if(num2):
   print("4.Inside if condition")

num1 = 1
num2 = 0
if(num1 or num2):
   print("5.Inside if condition")

num1 = 1
num2 = 0
if(num1 and num2):
   print("6.Inside if condition")

array1 = [1.5, "hi", 3, True]
if("hi" in array1):
  print("7.Inside if condition")

array1 = [1.5,"hi",3, True]
if(5 in array1):
  print("8.Inside if condition")

if("py" in "python"):
  print("9.Inside if condition")

# if("py" in "python") # without : sign
#    print("10.Inside if condition")

if 'cat' in ['dog', 'cat', 'horse', 'penguin']:
   print('Cat exists')
   print('Cat is my favourite pet')

if 'horse' in ('dog', 'cat', 'horse', 'penguin'):
  print('horse exists')
  print('horse is a strong animal')
  print('Cat is my favourite pet')

if 'horse' in ('dog', 'cat', 'horse', 'penguin'):
  print('horse exists')
if 'cat' in ('dog', 'cat', 'sheep'):
  print('cat exist')
if 'sheep' not in ('dog', 'cat', 'horse', 'penguin'):
  print('sheep does not exist')

a = 4
b = 7
if a > 0 and b > 0:
   print('Both are Positive numbers')
if a%2 or b%2:
   print('Either of one is even')
if a > 0 and not b < 0:
   print("Both are positive")

x = 10
y = 17
if (x > 0):
   print("X is positive")
if (x % 2 ==0):
   print("X is even")
if (y!=x):
   print("Both are unique")
if (y % 2 != 0):
   print("y is odd")
if (x>=11):
   print("condition is True")
if (y<=19):
  print("True")

a = 5
b = 10
c = 115
if a + b <= 99:
   print('a & b are two digit numbers')
if a + c <= 99:
   print('a & c are two digit numbers')
if a > 0:
   print(c / a)
if b > 0:
   print(c / b)
if c % b == 0:
   print("The numbers are divisible")
if c % a == 0:
   print("a is divisible by c")
if a < b < c:
    print(a + b + c)