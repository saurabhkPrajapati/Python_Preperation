# Example:

numbers = [1, 2, 3, 4, 5]

# Create a new list with squared values if the number is even,
# cubed values if the number is divisible by 3,
# and doubled values for all other cases
result = [x_squared if (x_squared := x**2) % 2 == 0 else (x_cubed if (x_cubed := x**3) % 3 == 0 else x*2) for x in numbers]

print(result)
