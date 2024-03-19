import time
from multiprocessing import Pool, cpu_count


def factorize_single(number):
    """Функція для обчислення дільників одного числа."""
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def factorize_parallel(*numbers):
    """Функція для паралельного обчислення дільників чисел."""
    with Pool(processes=cpu_count()) as pool:
        result = pool.map(factorize_single, numbers)
    return result


# Тестування паралельної функції
if __name__ == "__main__":
    start_time = time.time()
    a, b, c, d = factorize_parallel(128, 255, 99999, 10651060)
    print(f"Result for 128: {a}")
    print(f"Result for 255: {b}")
    print(f"Result for 99999: {c}")
    print(f"Result for 10651060: {d}")
    end_time = time.time()
    print(f"Parallel execution time: {end_time - start_time} seconds")
    # РЕЗУЛЬТАТ Parallel execution time: 0.860525369644165 seconds
