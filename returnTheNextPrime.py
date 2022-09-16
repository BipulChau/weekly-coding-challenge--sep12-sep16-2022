def check_prime_number(number):
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                return False
        return True
    return False


def next_prime_num(number):
    if check_prime_number(number):
        return number
    else:
        number += 1
        return next_prime_num(number)


print(check_prime_number(12))  # False
print(check_prime_number(24))  # False
print(check_prime_number(11), end="\n\n")  # True

print(next_prime_num(12))  # 13
print(next_prime_num(24))  # 29
print(next_prime_num(11))  # 11
