number = [44, 443, 44, 224, 8787, 56766, 4546, 3434, 675454, 76,434234]
size = len(number)
print(number)
# print("Enter first index to swap:")
# first_index = int(input())
# print("Enter Second index:")
# second_index = int(input())
# temp = number[first_index-1]
# number[first_index-1] = number[second_index-1]
# number[second_index-1] = temp
# print(number)
# print(max(number))
# print(min(number))
# print("Enter number to search:")
# test = int(input())
# if test in number:
#     print("Yes " + str(test) + " in list")
# else:
#     print(str(test)+ " is  not in list")
#print(number[::-1])
#Count occurence of number in list
# print("Enter Number to count no of occurence:")
# temp1 = int(input())
# count = 0
# for i in range(len(number)):
#     if temp1 == number[i]:
#         count = count+1
# print(count)
#Find Sum an Average of element in list
# sum = 0
# for i in range(len(number)):
#     sum = sum + number[i]
# average = sum/len(number)
# print("Sum of List Element = " + str(sum) + " and Average = " + str(average))

#Multiply all element of list with given number

# print("Enter number to multiply in list:")
# temp2 = int(input())
# for i  in range(size):
#     print(number[i]*temp2, end=' ')
#Calculate the all element digit sum in list
newList = []
digitSum = 0
for i in range(size):
    while number[i] > 0:
        rem = number[i] % 10
        digitSum = digitSum + rem
        number[i] = int(number[i]/10)
    newList.append(int(digitSum))
    digitSum = 0
print(newList)