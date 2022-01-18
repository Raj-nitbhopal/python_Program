# Program to Check Armstrong Number
print("Enter A Number:")
number = input()
result = 0
temp = int(number)
while temp > 0:
    rem = int(temp % 10)
    result = result + (rem * rem * rem)
    temp = int(temp/10)
if int(number) == int(result):
    print("Given Number " + str(number) + " is Armstrong number")
else:
    print("Given Number " + str(number) + " is Not Armstrong number")


