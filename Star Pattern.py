print("Enter A Number:")
number = int(input())
i = 1
j = 1
for i in range(1, number+1):
    for j in range(1, i+1):
        print(' * ', end='')
    print(" ")