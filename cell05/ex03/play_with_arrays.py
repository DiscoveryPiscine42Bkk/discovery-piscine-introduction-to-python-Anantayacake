original = [2, 8, 9, 48, 8, 22, -12, 2]
print(original)
new_set = {x + 2 for x in original if x > 5}
print(new_set)