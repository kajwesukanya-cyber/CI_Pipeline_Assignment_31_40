def remove_duplicates(numbers):
    return list(dict.fromkeys(numbers))


if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 4, 4, 5]

    print("Original List:", numbers)
    print("After Removing Duplicates:", remove_duplicates(numbers))
    