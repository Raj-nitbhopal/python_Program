# Python program to illustrate if-elif-else
#!/usr/bin/python
# Variable Declaration section
check_variable = 20
#Program logic section
if  (check_variable == 2):
    print ("check_variable is 2")
elif (check_variable == 4):
    print ("check_variable is 4")
elif (check_variable == 6):
    print ("check_variable is 6")
elif (check_variable == 8):
    print ("check_variable is 8")
elif (check_variable == 10):
    print ("check_variable is 10")
elif (check_variable == 12):
    print ("check_variable is 12")
elif (check_variable == 14):
    print ("check_variable is 14")
elif (check_variable == 16):
    print ("check_variable is 16")
elif (check_variable == 18):
    print ("check_variable is 18")
elif (check_variable == 20):
    print ("check_variable is 20")
else:
    print ("check_variable is not present")

Input_value = int(input(" Factorial Number : "))
factorial = 1
if Input_value  < 0:
    print(" Negative number cannot be placed for factorial determination ")
elif Input_value  == 0:
    print(" No factorial value for zero ")
else:
    for i in range(1, Input_value + 1):
        factorial = factorial*i
print("Value for the factorial " , Input_value  , "is" , factorial)
