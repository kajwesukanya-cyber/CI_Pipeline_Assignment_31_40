def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(is_sorted(numbers))
    