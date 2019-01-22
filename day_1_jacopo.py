import time

def isprime(n):
    for k in range(2, n):
        if n % k == 0:
            return False
    return True


def get_primes():
    n = 1
    while True:
        if isprime(n):
            yield n
        n += 1

for prime in get_primes():
    print(prime)
    time.sleep(1)

def doubler(f):
    print(f'I am doubler, called with {f}')
    def actual_function(n):
        print(f'I am actual_function, called with {n}')
        return f(n) * 2

    return actual_function


def plusone(x):
    return x + 1

mynewf = doubler(plusone)
print(mynewf(3))
print(mynewf(4))

import time

def log_in_out(original_fun):
    def logged_function(arg):
        print(f'they are invoking it with {arg}')
        result = original_fun(arg)
        print(f'the result it gave was {result}')
        return result
    return logged_function

@log_in_out
def dosomething(k):
    time.sleep(3)
    return k + 1

print(dosomething(34))