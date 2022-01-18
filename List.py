#List example in Python
# fruits = ["Apple", "Grapes", "Coconut", "Mango", "Pineapple", "Jackfruit", "Papaya"]
# print(fruits)
# print(fruits[0:4:2])
# print(fruits[2::2])
# print(fruits[::-1])
# city = ["Patna", "Patliputra", "Samastipur", "Motihari", "Dhaka", "Rampur", "Utter Pradesh", "Madhya Pradesh"]
# print(city)
# print(city[::])
# print(city[0:10:2])
# print(city[::-1])
# name = ["Rajan Kumar", "Sonu Kumar", "Anjani Kumar", "Anjali Kumari", "Sunny Kumar", "Krishnandan Kumar", "Chanchal Kumar"]
# print(name[0:9])
# print(name[::-1])
# print(name)
# name.append("Alok Ranjan Kumar")
# name.sort()
# print(name)
# name.__delitem__(6)
# print(name)
# print(name.count("Rajan Kumar")) # count function specified value in list
# if "Rajan Kumar" in name:
#     print("Yes it is present")
# name.remove("Rajan Kumar") # remove takes one parameter
# name.insert(4, "Rajan Kumar")
# name.extend(city)
# name.reverse()
# name.pop(5)
# name.sort(reverse = True)
# print(name)
# for i in name:
#      print(i)
# for i in range(len(name)):
#     print(i)
num = [44, 55, 6, 7, 3, 6, 4, 6, 3, 6, 754, 34, 454, 43, "rajan"]
for i in num:
    if str(i).isnumeric() and i > 6:
        print(i)