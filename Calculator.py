value = {45 * 3: 555, 56 + 9: 77, 56/7: 5}
print("Enter First Number:")
n = input()
print("Enter Second Number:")
m = input()

print("Sum of " + n + " and " + m + " is " + str(int(n)+int(m)))
print("Absolute Difference of " + n + " and " + m + " is " + str(abs(int(n)-int(m))))
print("Multiplication of " + n + " and " + m + " is " + str(int(n)*int(m)))
for item in value:
    print(item)