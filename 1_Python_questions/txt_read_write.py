# Writing a string to a file
with open('example.txt', 'w') as file:
    file.write('Hello, world!\n')
    file.write('This is the first line.\n')
    file.write('This is the second line.\n')

# ____________________________________________________

# Reading all lines from the file and returning a list
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print("All lines using readlines():")
    print(lines)

# ____________________________________________________

# Reading the entire content of the file into a string
with open('example.txt', 'r') as file:
    content = file.read()
    print("File content using read():")
    print(content)
