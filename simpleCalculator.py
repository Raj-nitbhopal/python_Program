# A Simple calculator program using dictionary as Switch Case

# def Addition(x, y):
#     return x + y
# def Substraction(x, y):
#     return x - y
# def Multiplication(x, y):
#     return x * y
# def Division(x, y):
#     return x / y
# def Modulo(x, y):
#     return x % y
#
#  def calculator(argument)
#      switcher = {
#          1 : Addition(),
#          2 : Substraction(),
#          3 : Multiplication(),
#          4 : Division(),
#          5 : Modulo()
#      }
#      return switcher.get(argument, "Invalid Choice")


if __name__ == "__main__":
    print('Enter First Number:')
    num1 = int(input())
    print('Enter Second Number:')
    num2 = int(input())
    print('1: Addition')
    print('2: Substraction')
    print('3: Multiplication')
    print('4: Division')
    print('5: Remainder')
    print("\n Enter Choice: ")
    choice = int(input())

    choice = {
        1: print("Sum of " + str(num1) + " and " + str(num2) + " is " + str(num1 + num2)),
        2: print("Substraction of " + str(num1) + " and " + str(num2) + " is " + str(num1 - num2)),
        3: print("Multiplication of " + str(num1) + " and " + str(num2) + " is " + str(num1 * num2)),
        4: print("Division of " + str(num1) + " and " + str(num2) + " is " + str(num1 / num2)),
        5: print("Remainder of " + str(num1) + " and " + str(num2) + " is " + str(num1 % num2))

    }
