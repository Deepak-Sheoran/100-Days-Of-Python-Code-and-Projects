# Instructions
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
#
#
# You need to write a function that checks whether if the number passed into it is a prime number or not.
#
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
#
# But 4 is not a prime number because you can divide it by 1, 2 or 4

def prime_checker(number):
    multiples = [2, 3, 5, 7]
    if number in multiples:
        print("It's a prime number.")
        return True
    for multiple in multiples:
        if number % multiple == 0 or number == 1:
            print("It's not a prime number.")
            return False
    return True


primes = []

for num in range(1, 101):
    print(num, " - ", end=" ")
    check = prime_checker(num)
    if check:
        primes.append(num)

print(f"Prime numbers between 1 and 100 = {primes}")
