# Given sets
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

# 1. Add element 60 using add()
s1.add(60)
print("After adding 60:", s1)


# 2. Add multiple elements using update()
s1.update([70, 80, 90])
print("After update:", s1)


# 3. Remove element 20 using remove()
s1.remove(20)
print("After removing 20:", s1)


# 4. Remove element 100 safely using discard()
s1.discard(100)
print("After discard 100:", s1)


# 5. Remove random element using pop()
removed = s1.pop()
print("Popped element:", removed)
print("Remaining set:", s1)


# 6. Copy set and modify copy
copy_set = s1.copy()
copy_set.add(999)
print("Original set:", s1)
print("Modified copy:", copy_set)


# 7. Clear all elements
s1.clear()
print("After clear:", s1)
print("Length:", len(s1))


# 8. Convert list with duplicates to set
lst = [1, 2, 2, 3, 3, 4]
new_set = set(lst)
print("Set from list:", new_set)


# 9. Convert set to list and sort
sorted_list = list(new_set)
sorted_list.sort()
print("Sorted list:", sorted_list)