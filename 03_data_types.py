print("\n1. Getting Data Type with type():")
x = 5
print("x =", x, "| Type:", type(x))
x = "Hello World"
print("x =", x, "| Type:", type(x))
x = 20.5
print("x = ", x, "| Type:", type(x))

print("\n2. Text Type (String):")
x = "Hello World"
print("String:", x, "| Type:", type(x))

print("\n3. Numeric Types:")
x = 20
print("x =", x, "| Type:", type(x))
x = 20.5
print("x =", x, "| Type:", type(x))
x = 1j
print("x =", x, "| Type:", type(x))

print("\n4. Sequence Types:")
x = ["apple", "banana", "cherry"]
print("List:", x, "| Type:", type(x))
x = ("apple", "banana", "cherry")
print("Tuple:", x, "| Type:", type(x))
x = range(6)
print("Range:", x, " Type:", type(x))
print("Range Values:", list(x))

print("\n5. Mapping Type:")
x = {"name": "John", "age": 36}
print("Dictionary:", x, "| Type:", type(x))

print("\n6. Set Types:")
x = {"apple", "banana", "cherry"}
print("Set:", x, "| Type:", type(x))
x = frozenset({"apple", "banana", "cherry"})
print("Frozenset:", x, "| Type:", type(x))

print("\n7. Boolean Type:")
x = True
print("Boolean True:", x, "| Type:", type(x))
x = False
print("Boolean False:", x, "| Type:", type(x))

print("\n8. Binary Types:")
x = b"Hello"
print("Bytes:", x, "| Type:", type(x))
x = bytearray(5)
print("Bytearray:", x, "| Type:", type(x))
x = memoryview(bytes(5))
print("Memoryview:", x, "| Type:", type(x))

print("\n9. None Type:")
x = None
print("None:", x, "| Type:", type(x))

print("\n10. Setting Specific Data Types:")
x = str("Hello World")
print("str():", x, "| Type:", type(x))
x = int(20)
print("int():", x, "| Type:", type(x))
x = float(20.5)
print("float():", x, "| Type:", type(x))
x = complex(1j)
print("complex():", x, "| Type:", type(x))
x = list(("apple", "banana", "cherry"))
print("list():", x, "| Type:", type(x))
x = tuple(("apple", "banana", "cherry"))
print("tuple():", x, "| Type:", type(x))
x = dict(name="John", age=36)
print("dict():", x, "| Type:", type(x))
x = set(("apple", "banana", "cherry"))
print("set():", x, "| Type:", type(x))
x = frozenset(("apple", "banana", "cherry"))
print("frozenset():", x, "| Type:", type(x))
x = bool(5)
print("bool():", x, "| Type:", type(x))
x = bytes(5)
print("bytes():", x, "| Type:", type(x))
x = bytearray(5)
print("bytearray():", x, "| Type:", type(x))
x = memoryview(bytes(5))
print("memoryview():", x, "| Type:", type(x))

print("\n11. Practical Examples for AI/CS:")
student_name = "Mehedi Fahim"
student_id = 10
student_gpa = 3.42
is_enrolled = True
courses = ["AI Lab", "Data Mining", "Pattern Recognition"]
grades = ("A+", "A+", "A")
student_info = {
    "name": "Mehedi Fahim",
    "id": 10,
    "department": "CSE",
    "semester": 7
}
print("Student Name:", student_name, "| Type:", type(student_name))
print("Student ID:", student_id, "| Type:", type(student_id))
print("Student GPA:", student_gpa, "| Type:", type(student_gpa))
print("Is Enrolled:", is_enrolled, "| Type:", type(is_enrolled))
print("Courses:", courses, "| Type:", type(courses))
print("Grades:", grades, "| Type:", type(grades))
print("Student Info:", student_info, "| Type:", type(student_info))

print("\n12. Type Checking Examples:")
def check_data_type(data):
    if isinstance(data, str):
        return f"'{data}' is a string"
    elif isinstance(data, bool):
        return f"'{data}' is a boolean"
    elif isinstance(data, float):
        return f"'{data}' is a float"
    elif isinstance(data, int):
        return f"'{data}' is an integer"
    elif isinstance(data, list):
        return f"'{data}' is a list"
    else:
        return f"'{data}' is of type {type(data)}"
test_data = ["Hello", 42, 3.14, True, [1, 2, 3]]
for item in test_data:
    print(check_data_type(item))
