#Ask user for number higher than zero
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            #ask the user for an input
            response = float(input(question))

            #check the number is more than zero
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

keep_going = ""
while keep_going == "":
    width = num_check("Width: ")
    height = num_check("Height: ")
    cost = num_check("Cost per meter: ")

    #Calculate perimeter and fence cost
    perimeter = 2 * (width+height)
    price = perimeter * cost

    print()
    print(f"Perimeter: {perimeter}12 units")
    print(f"Price: ${price:.2f}")
    keep_going = input("Press enter to use the program again or any key to quit")

print("\nThank you for using the area / perimeter calculator :):):):)):)")