import random
import time

import rust_pyo3

INT32_MAX = 2 ** 31 - 1


def sum_as_string(a: int, b: int) -> str:
    return str(a + b)


def test_rust_metrics() -> int:
    t = time.perf_counter()
    for _ in range(1_000_000):
        rust_pyo3.sum_as_string(
            random.randint(0, INT32_MAX),
            random.randint(0, INT32_MAX),
        )
    return time.perf_counter() - t


def test_python_metrics() -> int:
    t = time.perf_counter()
    for _ in range(1_000_000):
        sum_as_string(
            random.randint(0, INT32_MAX),
            random.randint(0, INT32_MAX),
        )
    return time.perf_counter() - t


if __name__ == "__main__":
    python_metrics = test_python_metrics()
    rust_metrics = test_rust_metrics()
    print(f"Rust: {rust_metrics} s / Python: {python_metrics} s")
