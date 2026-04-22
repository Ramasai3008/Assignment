data = [10, 20, 30, 40, 50, 20, 30, 60, 70, 80, 90]
print("Initial list:", data)

# 1.append()
data.append([100, 110])
print("After append:", data)


# 2.extend()
data.extend([120, 130])
print("After extend:", data)


# 3.insert()
data.insert(2, 25)
print("After insert:", data)


# 4.remove()
data.remove(20)
print("After remove:", data)


# 5.pop()
last_element = data.pop()
print("After pop:", data)
print("Popped element:", last_element)


# 6.count()
count = data.count(30)
print("Count of 30:", count)

# 7.index()
index_40 = data.index(40)
print("Index of 40:", index_40)


# 8.reverse()
data.reverse()
print("After reverse:", data)

# 9.sort() issue
data.remove([100,110])
data.sort()
print("sort() issue:", data)