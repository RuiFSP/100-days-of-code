# bad practice example

# file open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# good practice
# default on mode is r - read
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# we can open/write immediately if the file does not exist
with open("new_file_.txt", mode="w") as file:
    file.write("new file wiii.")
