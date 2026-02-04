import sys

# print(sys.version)
# print(sys.path)
# print(sys.modules)   # sys.modules return the name of the Python modules that the current shell has imported.
# print(sys.getdefaultencoding())  # Print the current string encoding used
#############
# sys.path = []
# from fastapi import FastAPI    # ModuleNotFoundError: No module named 'fastapi'
#############
################################
# print('Enter Text:', end='\n')
# for line in sys.stdin:
#     # print('Enter Text') # this cannot be printed
#     if 'q' == line.rstrip():
#         break
#     sys.stdout.write(f'Input : {line}\n')
#
# sys.stdout.write('Exit\n')

# ########################
# def print_to_stderr(a: str):
#     print(a, file=sys.stderr)  # for printing error

# print_to_stderr("Error")
# print_to_stderr()

######################
# age = 6
# if age < 18:
#     # exits the program
#     # sys.exit("Age less than 18")  # Process finished with exit code 1
#     sys.exit(200)   # Process finished with exit code 200
# else:
#     print("Age is not less than 18")
#######

from sys import stdin
my_input = stdin.read(4)
sys.stdout.write("\n")
my_input2 = stdin.readline()
total = int(my_input2)
print("my_input = {}".format(my_input))
print("my_input2 = {}".format(my_input2))
print("total = {}".format(total))

# sys.exc_info()   (type, value, traceback)

