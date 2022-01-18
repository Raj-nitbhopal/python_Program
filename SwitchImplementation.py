# Switch Case Implementation using If-else
def get_week_day(argument):
    if(argument == 0):
        day="Sunday"
    elif(argument == 1):
        day="Monday"
    elif(argument == 2):
        day="Tuesday"
    elif(argument == 3):
        day="Wednesday"
    elif(argument == 4):
        day="Thursday"
    elif(argument == 5):
        day="Friday"
    elif(argument == 6):
        day="Saturday"
    else:
      day="Invalid day"
    return day
# Driver program
if __name__ == "__main__":
    print (get_week_day(6))
    print (get_week_day(8))
    print (get_week_day(0))


# Switch Implementation using Dicctionary

def set_week_day(argument):
    all_day = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thrusday",
        5: "Friday",
        6: "Saturday"
    }
    return all_day.get(argument, "Invalid Day")
if __name__ == "__main__":
    print (set_week_day(6))
    print (set_week_day(3))


# def get_week_day(argument):
#       def zero():
#         return "Sunday"
#       def one():
#         return "Monday"
#       def two():
#         return "Tuesday"
#       def three():
#         return "Wednesday"
#       def four():
#         return "Thursday"
#       def five():
#         return "Friday"
#       def six():
#         return "Saturday"
#         switcher = {
#         0: zero(),
#         1: one(),
#         2: two(),
#         3: three(),
#         4: four(),
#         5: five(),
#         6: six()
#         }
#     return switcher.get(argument)
#
#
# # Driver program
# if __name__ == "__main__":
#     print (get_week_day(6))
#     print (get_week_day(8))
#     print (get_week_day(0))
