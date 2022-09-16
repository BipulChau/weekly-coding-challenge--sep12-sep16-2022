def check_prime_number(number):
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                return False
            else:
                return True


def return_the_next_prime(number):
    if check_prime_number(number):
        return number
    else:
        number += 1
        return_the_next_prime(number)
        # print(number)



print(check_prime_number(12))  # False
print(check_prime_number(24))  # False
print(check_prime_number(11))  # True

print(return_the_next_prime(12)) # 13
print(return_the_next_prime(24)) # 25
print(return_the_next_prime(11)) # 11
