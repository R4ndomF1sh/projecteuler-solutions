number = 2
max_count = int(input("max? "))
count = 0

def test_primenumber(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

while count < max_count:
    if test_primenumber(number):
        prime_number = number
        count += 1
    number += 1

print(prime_number)