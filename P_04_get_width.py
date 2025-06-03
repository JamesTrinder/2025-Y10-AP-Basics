# Ask a user for width and loop until they
# give an answer that is more than zero

error = "Please enter a number that is more than zero\n"
while True:

    try:
        #ask the user for an input
        width = float(input("Width: "))

        #check the number is more than zero
        if width > 0:
            break
        else:
            print(error)
    except ValueError:
        print(error)