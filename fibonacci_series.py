def generate_fibonacci(n):
    series = []

    a, b = 0, 1

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series


def main():
    try:
        n = int(input("Enter number of terms: "))

        if n <= 0:
            print("Enter a positive number.")
            return

        series = generate_fibonacci(n)

        print("Fibonacci Series:")
        print(*series)

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
