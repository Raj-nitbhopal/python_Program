# mynumber = 25
# count = 5
# guessNumber = int(input("Guess The Number\n"))
# if guessNumber == mynumber:
#     print("Your guess is correct")
# elif guessNumber > mynumber:
#     print("Plz guess less than ", guessNumber)
#     print("Your remaining chance is ", count-1)
# elif guessNumber < mynumber:
#     print("Plz guess greater than ", guessNumber)
#     print("Your remaining chance is", count-2)

numList = (11, 21, 13, 41)
res = map(lambda x: x + x, numList)
print(list(res))
