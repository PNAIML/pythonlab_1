# Creating a tuple
colors = ("red", "green", "blue")
print("Original tuple:", colors)

# Accessing elements
print("First color:", colors[0])
print("Last color:", colors[-1])

# Slicing a tuple
print("First two colors:", colors[:2])

# Checking membership
print("Is 'green' in the tuple?", "green" in colors)

# Tuple length
print("Number of colors:", len(colors))

# Nested tuples
nested = (1, 2, ("a", "b"))
print("Nested tuple:", nested)
print("Element from nested tuple:", nested[2][1])

# Tuple concatenation
new_colors = colors + ("yellow", "purple")
print("Concatenated tuple:", new_colors)

# Repetition
repeat = ("hi",) * 3
print("Repeated tuple:", repeat)

new_colors.sort()
