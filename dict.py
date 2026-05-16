# Dictionary Program Practice

data = {
    "name": "Sangeetha",
    "age": 18,
    "course": "Python"
}

# Print complete dictionary
print(data)

# Access value
print(data["name"])

# Using get()
print(data.get("course"))

# Key not present
print(data.get("marks"))

# get() with default value
print(data.get("marks", "Not Found"))

# Add new item
data["marks"] = 95
print(data)

# Update value
data["age"] = 19
print(data)

# Delete item
del data["course"]
print(data)

# Print keys
print(data.keys())

# Print values
print(data.values())

# Print key and value using loop
for key, value in data.items():
    print(key, ":", value)

# Count total items
print(len(data))

# Check key exists
if "name" in data:
    print("Key Exists")
else:
    print("Key Not Found")

# Copy dictionary
new_data = data.copy()
print(new_data)

# Clear dictionary
new_data.clear()
print(new_data)

# zip() example
keys = ["a", "b", "c"]
values = [10, 20, 30]

dict1 = dict(zip(keys, values))
print(dict1)

# Nested dictionary
student = {
    "name": "Anu",
    "marks": {
        "math": 90,
        "science": 95
    }
}

print(student["marks"]["math"])

# Dictionary with list
prog = {
    "Python": ["PyCharm", "VS Code"],
    "Java": ["NetBeans", "Eclipse"]
}

print(prog["Python"][1])
