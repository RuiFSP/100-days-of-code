# key Error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existing_key"]

# index Error
# fruit_list = ["apple", "bana", "pear"]
# fruit = fruit_list[3]

#type Error
# text = "abc"
# print(text + 5)

# file not found
# try:
#     # something that might cause an exception
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     # do this if there was an execution
#     open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")
#     # raise as exception
#     raise KeyError

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)