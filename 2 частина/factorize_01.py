import time


def factorize_single(number):
    """Функція для обчислення дільників одного числа."""
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def factorize(*numbers):
    """Функція, яка приймає список чисел та повертає список їх дільників."""
    result = []
    for number in numbers:
        result.append(factorize_single(number))
    return result


# Тестування функції
if __name__ == "__main__":
    start_time = time.time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print(f"Result for 128: {a}")
    print(f"Result for 255: {b}")
    print(f"Result for 99999: {c}")
    print(f"Result for 10651060: {d}")
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
    # РЕЗУЛЬТАТ Execution time: 0.5845210552215576 seconds
