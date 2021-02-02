a = "Hello, World!"
print(a.upper()) # Make all letters big
a = "Hello, World!"
print(a.lower()) # make all letter small
b = "                   Hello, World!                      "
print(b.strip()) # returns "Hello, World!" Deletes all spaces
print(b)


a = "HHello,  Hello  Jim  World!"
print(a.replace("H", "J"))


a = "Hello, World!"
print(a.split("o")) # returns ['Hello', ' World!']