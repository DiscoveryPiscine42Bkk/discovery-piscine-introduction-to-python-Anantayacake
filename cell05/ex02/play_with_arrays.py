original = [2, 8, 9, 48, 8, 22, -12, 2]
print(original)
new_array = []
for number in original:
    if number > 5:
        new_array.append(number + 2)
print(new_array)
