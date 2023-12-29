from org.lib.bar import get_fibonacci, get_primes


def main() -> None:
    fibonacci = get_fibonacci()
    fibonacci_sum = fibonacci.sum()
    print(f"Here is the sum of some Fibonacci numbers: {fibonacci_sum}")

    primes = get_primes()
    primes_sum = primes.sum()
    print(f"Here is the sum of some prime numbers: {primes_sum}")


if __name__ == "__main__":
    main()
