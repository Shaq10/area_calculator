''' 
This program calculates the area of a shape chosen by the user 

'''

print ("Program is running") #inform user that program is running
option = input("Enter C for Circle or T for Triangle: ") #ask user for shape choice
option = option.lower()

#calculate area of circle for given radius
if option == 'c':
    radius = float(input("Enter the radius: "))
    area = 3.14159 * (radius ** 2)
    print ("Area: %f" % area)

#calculate area of triangle for given base and height
elif option == 't':
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print ("Area: %f" % area)

#message if shape is invalid
else:
    print ("Invalid input from user!")

print ("Exiting...")
