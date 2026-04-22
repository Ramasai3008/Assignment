student = {
    "name": "John",
    "age": 21,
    "marks": {"math": 80, "science": 90}
}

print("Initial dictionary:", student)

# 1.Access name using get()
print("Name:", student.get("name"))


# 2.Update age using update()
student.update({"grade": "A"})
print("After updating grade:", student)


# 3. Update age using update()
student.update({"age": 22})
print("After updating age:", student)

# 4. Remove age using pop()
removed_age = student.pop("age")
print("After removing age:", student)
print("Removed age:", removed_age)

# 5. Remove last inserted item using popitem()
last_item = student.popitem()
print("After popitem:", student)
print("Removed last item:", last_item)

# 6. Get all keys
print("Keys:", student.keys())

# 7. Get all values
print("Values:", student.values())

# 8. Get all items
print("Items:", student.items())

# 9. Use setdefault() to add city
student.setdefault("city", "New York")
print("After setdefault (city):", student)

# 10. Merge another dictionary

college = {
    "CSE": ["Ravi", "Sita"]
}

student.update(college)
print(student)