def factorial(n):
    return 1 if n == 0 else factorial(n - 1) * n

if __name__ == "__main__":
    print(factorial(0) == 1)
    print(factorial(3) == 6)
    print(factorial(4) == 24)
