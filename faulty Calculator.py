# Statement: if entry is 45*3, 56/8, 65 +34 print result 555, 4, 77 respectively
num1 = int(input("Enter First Number\n"))
num2 = int(input("Enter Second Number\n"))
num3 = input("Choose Operator +, -, *, /, **, % \n")

if num3 == '+':
    if num1 == 65 and num2 == 34:
        print(77)
    else:
        print(num1 + num2)

if num3 == '*':
    if num1 == 45 and num2 == 3:
        print(555)
    else:
        print(num1 * num2)

if num3 == '/':
    if num1 == 65 and num2 == 8:
        print(4)
    else:
        print(num1 / num2)
if num3 == '**':
        print(num1 ** num2)

if num3 == '-':
        print(num1 - num2)
if num3 == '%':
        print(num1 % num2)