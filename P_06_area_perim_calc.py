#Ask user for width and height
#(assume they put in valid data
width = float(input("Width: "))
height = float(input("Height: "))

#calculate the area / perimeter
area = width * height
perimeter = 2 * (width+height)

#output the area / perimeter
print()
print(f"Perimeter: {perimeter} units")
print(f"Area: {area} square units")