# Creating a dictionary
student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
print("Original dictionary:", student)
# Accessing values
print("Student's name:", student["name"])
print("Student's age:", student.get("age"))
# Adding a new key-value pair
student["grade"] = "A"
print("After adding grade:", student)
# Updating a value
student["age"] = 22
print("After updating age:", student)
# Removing a key-value pair
del student["major"]
print("After deleting major:", student)
# Iterating through keys and values
print("Student details:")
for key, value in student.items():
    print(key, ":", value)

# Checking for a key
print("Does 'grade' exist?", "grade" in student)

# Getting all keys and values
print("Keys:", student.keys())
print("Values:", student.values())
student.keys()
