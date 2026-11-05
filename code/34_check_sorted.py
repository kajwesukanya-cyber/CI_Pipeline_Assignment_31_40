def is_sorted(numbers):
    return numbers == sorted(numbers)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("List is sorted:", is_sorted(numbers))