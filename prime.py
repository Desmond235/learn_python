def prime_factors(n: int) -> dict:
    factors: dict = {}
    divisor: int = 2
    while divisor <= n / divisor:
        while n % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            n //= divisor
        divisor += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def find_lcm(a: int, b: int) -> int:
    factors_of_a: dict = prime_factors(a)
    factors_of_b: dict = prime_factors(b)
    lcm_factors: dict = {}

    all_prime_factors: set = set(factors_of_a.keys()) | set(factors_of_b.keys())
    for prime in all_prime_factors:
        power_a = factors_of_a.get(prime, 0)
        power_b = factors_of_b.get(prime, 0)
        lcm_factors[prime] = max(power_a, power_b)
    lcm = 1
    for key, value in lcm_factors.items():
        lcm *= pow(key, value)
    return lcm

if __name__ == "__main__":
    print("This program finds the LCM for two numbers")
    print("Enter two numbers")
    number1 = input()
    number2 = input()
    
    if not number1.isdigit() or not number2.isdigit():
        print('what you entered is not a number, exiting....')
    if number1.isdigit() and  number2.isdigit():
        lcm = find_lcm(int(number1), int(number2))
        print(f"The LCM for {number1} and {number2} is: {lcm}")       
