print("Enter the Year:")
year = input()
if int(year) % 100 == 0:
    if int(year) % 400 == 0:
        print(year + " is a Leap Year")
    else:
        print(year + " is  not a Leap Year")
elif int(year) % 4 == 0:
    print(year + " is a Leap Year")
else:
    print(year + "i s not a Leap Year")