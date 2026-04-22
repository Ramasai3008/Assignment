t = (10, 20, 30, 40, 50, 20, 60)
print("Initial tuple:", t)


# 1.Count occurrences of 20
print("Count of 20:", t.count(20))


# 2.Find index of 40
print("Index of 40:", t.index(40))


# 3.Convert to list, append 70, convert back
temp = list(t)
temp.append(70)
t = tuple(temp)
print("After adding 70:", t)


# 4.Slice from index 2 to 5
print("Sliced tuple (2 to 5):", t[2:6])


# 5. Concatenate another tuple
t = t + (80, 90)
print("After concatenation:", t)


# 6. Repeat tuple 2 times
t_repeated = t * 2
print("Repeated tuple:", t_repeated)

'''
# 7. Check if 50 exists
print("Is 50 present?", 50 in t)

# 8. Unpack tuple into variables
a, b, c, d, e, f, g, h, i = t
print("Unpacked values:", a, b, c, d, e, f, g, h, i)

# 9. Try modifying element (immutability)
try:
    t[0] = 100
except TypeError as e:
    print("Error:", e)

# 10. Nested tuple and access inner value
nested = (1, 2, (3, 4, 5), 6)
print("Nested tuple:", nested)
print("Access inner value (4):", nested[2][1])

'''