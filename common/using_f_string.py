# for format

name = "Alex"
string_hello = f"Hello {name}"
print(string_hello)

i = 10
print(f"{i} squared is {i * i}")

# concatenate
list_of_string = ["hello", "my", "friend"]

# Bad way
concate_string = ""
for string in list_of_string:
    concate_string += string + " "
print(concate_string)

# good way
# concate_string = " ".join(list_of_string)
# concate_string = "".join(list_of_string)
concate_string = ",".join(list_of_string)
print(concate_string)
