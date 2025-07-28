num = 1


def check_prime():
    flag = True
    if num > 1:
        for i in range(2, num - 1):
            if num % i == 0:
                flag = False
                break
        return flag
    else:
        return False


print(check_prime())

# ______________________________________________________________________________


num = 8
if num > 1:
    for i in range(2, num-1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
