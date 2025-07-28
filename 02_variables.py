print("\n1. Creating Variables:")
x = 5
y = "Hello"
print("x =", x)
print("y =", y)

print("\n2. Dynamic Typing:")
x = 4
print("x =", x, "| Type:", type(x))
x = "Sally"
print("x =", x, "| Type:", type(x))

print("\n3. Valid Variable Names:")
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print("myvar =", myvar)
print("my_var =", my_var)
print("_my_var =", _my_var)
print("myVar =", myVar)
print("MYVAR =", MYVAR)
print("myvar2 =", myvar2)

print("\n4. Multiple Assignment:")
x, y, z = "Orange", "Banana", "Cherry"
print("x =", x)
print("y =", y)
print("z =", z)

print("\n5. Same Value to Multiple Variables:")
x = y = z = "Orange"
print("x =", x)
print("y =", y)
print("z =", z)

print("\n6. Unpacking a Collection:")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print("x =", x)
print("y =", y)
print("z =", z)

print("\n7. Output Variables:")
x = "Python is "
y = "awesome"
z = x + y
print(z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

print("\n8. Mathematical Operations:")
x = 5
y = 10
print("x + y =", x + y)

print("\n9. Global Variables:")
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()

print("\n10. Local VS Global Variables:")
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)

print("\n11. Using Global Keyword:")
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
    print("Inside function: Python is " + x)
myfunc()
print("Outside function: Python is " + x)

print("\n12. Different Variable Types:")
student_name = "Mehedi Fahim"
student_age = 22
student_gpa = 3.42
is_student = True
subjects = ["AI", "Data Mining", "Pattern Recognition"]
print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"GPA: {student_gpa}")
print(f"Is Student: {is_student}")
print(f"Subjects: {subjects}")
