year = 2000
leap = False
if year % 100 and year % 400 == 0:
    leap = True
elif year % 4 == 0:
    leap = True

print(leap)
