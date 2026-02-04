def print_formatted(number):
    # Get the width of the binary representation of the largest number
    width = len(bin(number)) - 2

    for i in range(1, number + 1):
        # Print decimal, octal, hexadecimal (uppercase), and binary representations
        print(f"{i:{width}d} {oct(i)[2:]:{width}} {hex(i)[2:].upper():{width}} {bin(i)[2:]:{width}}")


print_formatted(17)

# ________________________________________________________________________

binary = "1101"
decimal = int(binary, 2)  # Binary to decimal
print(decimal)


octal = "17"
decimal = int(octal, 8)  # Octal to decimal
print(decimal)


hexadecimal = "1A"
decimal = int(hexadecimal, 16)  # Hexadecimal to decimal
print(decimal)
