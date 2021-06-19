def get_primes(numbers):
    for number in numbers:
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
