piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

# slice list "cde"
print(piano_keys[2:5])

# slice list from [c, ... to the end]
print(piano_keys[2:])

# slice list with step 2
print(piano_keys[2:5:2])
print(piano_keys[::2])

# reverse list
print(piano_keys[::-1])

# similar operations for tuples

print(piano_tuple[1:])
