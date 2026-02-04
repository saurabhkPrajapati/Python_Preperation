def decimal_to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary


# Test
print(decimal_to_binary(13))  # Output: 1101



