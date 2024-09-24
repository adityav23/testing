import math

def prime_check(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def run_calculations():
    num = 29
    if prime_check(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

    a, b = 54, 24
    print(f"GCD of {a} and {b} is: {gcd(a, b)}")
    print(f"LCM of {a} and {b} is: {lcm(a, b)}")

    n = 10
    print(f"Fibonacci sequence of length {n}: {fibonacci(n)}")

    numbers = [10, 20, 30, 40, 50]
    print(f"Average of {numbers}: {calculate_average(numbers)}")

if __name__ == "__main__":
    run_calculations()
