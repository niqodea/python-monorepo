from org.lib.bar.numbers import get_fibonacci, get_primes


def test_fibonacci() -> None:
    numbers = get_fibonacci()

    assert numbers[0] == 0
    assert numbers[1] == 1

    for a, b, c in zip(numbers, numbers[1:], numbers[2:]):
        assert a + b == c


def test_primes() -> None:
    numbers = get_primes()

    for number in numbers:
        for potential_divisor in range(2, number):
            assert number % potential_divisor != 0
