
def move_zeros(arr):
    non_zeros = [num for num in arr if num != 0]
    zeros = [num for num in arr if num == 0]
    return non_zeros + zeros


if __name__ == "__main__":
    numbers = [0, 1, 0, 3, 12]
    print("Original List:", numbers)
    print("After Moving Zeros:", move_zeros(numbers))
    