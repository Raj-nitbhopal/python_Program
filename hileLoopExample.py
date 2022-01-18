# n = 10  # upper limit
# # initializes the variable for sum
# sum = 0
# i = 1
# while i <= n:
#     sum = sum + i
#     i = i + 1     #increment the counter
# # print the sum
# print("the sum :",  sum)
#
# n = 1
# print("Infinite loop starts")
# while n > 0:
#     if n > 20:
#         break
#     print(n)
#     n = n + 1
#
# n = 10
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i, " is Even Number")
#         i = i + 1
#     else:
#         print(i, " is Odd Number")
#         i = i + 1
while True:
    num = int(input("Enter a number \n"))
    if num > 100:
        print(" Printed greater than 100")
        break
    else:
        print("Try Again")
        continue

