# Ask a user for width and loop until they
# give an answer that is more than zero
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

# Main Routine Goes Here

keep_going = ""
while keep_going == "":

    # Get width and height

    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate area / perimeter

    area = width * height
    perimeter = 2 * (width+height)

    # Display output

    print(f"Area: {area} square units")
    print(f"Perimeter: {perimeter} units")

    # Ask user if they want to keep going
    keep_going = input("Press enter if you want to keep going or any key to quit. ")
    print()

print("Thank you for using the area / perimeter calculator")