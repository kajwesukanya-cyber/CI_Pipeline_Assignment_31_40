def most_frequent(numbers):
    if not numbers:
        return None

    return max(numbers, key=numbers.count)


if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 4, 2, 5]
    print("Most frequent element:", most_frequent(numbers))
    