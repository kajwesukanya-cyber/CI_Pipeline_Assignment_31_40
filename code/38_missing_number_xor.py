def find_missing_number(numbers):
    n = len(numbers) + 1
    missing = 0

    for i in range(1, n + 1):
        missing ^= i

    for num in numbers:
        missing ^= num

    return missing


if __name__ == "__main__":
    numbers = [1, 2, 4, 5]
    print("Missing number:", find_missing_number(numbers))
    