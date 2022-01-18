# Program to check Number is Palindrome or Not

print("Enter A Number to Check:")
number = input()
temp = int(number)
result = 0
while temp > 0:
    rem = int(temp % 10)
    result = result * 10 + rem
    temp = int(temp / 10)
if int(number) == int(result):
    print('Given Number ' + number + " is a Palindrome Number!!!")
else:
    print('Given Number ' + number + " is not a Palindrome Number!!!")