var_a = 1
var_b = 2
while var_a < var_b:
    print(" Code enters while loop ")
    var_c = ["SUV", "sedan", "hatchback", "End"]
    for iterator in var_c:
        if iterator == "SUV":
            print("Hyundai creata")
            print("Mahindra bolero")
            print("\n---------------")
        if iterator == "sedan":
            pass
        if iterator == "hatchback":
            print("Renault Kwid")
            print("suzuki alto")
            print("\n---------------")
        if iterator == "End":
            break
    var_a = var_a+1
