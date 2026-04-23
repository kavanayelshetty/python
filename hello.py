print("hello world")
a=10 
print(a)
l=["apple","mango","banana"]
print(l)
a=10
b=20
print(a&b)
print(a%b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
n = int(input("enter the value of N: "))
a=0
b=1
print("fibonacci sequence: ")
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
prefixes="JKLMN"
suffix="ack"
for p in prefixes:
    print(p+suffix)    
# Function to calculate area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Function to calculate area of a triangle
def calculate_triangle_area(base, height):
    return 0.5 * base * height

# --- Main Program ---

# Input for Rectangle
print("--- Rectangle Area Calculation ---")
rect_length = float(input("Enter the length of the rectangle: "))
rect_width = float(input("Enter the width of the rectangle: "))

# Input for Triangle
print("\n--- Triangle Area Calculation ---")
tri_base = float(input("Enter the base of the triangle: "))
tri_height = float(input("Enter the height of the triangle: "))

# Perform Calculations
rect_area = calculate_rectangle_area(rect_length, rect_width)
tri_area = calculate_triangle_area(tri_base, tri_height)

# Print Results
print(f"\nThe area of the rectangle is: {rect_area}")
print(f"The area of the triangle is: {tri_area}")

