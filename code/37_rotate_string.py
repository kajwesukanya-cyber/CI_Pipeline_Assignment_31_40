def rotate_string(text, k):
    if not text:
        return text

    k = k % len(text)
    return text[k:] + text[:k]


if __name__ == "__main__":
    text = input("Enter a string: ")
    k = int(input("Enter rotation positions: "))

    print("Rotated string:", rotate_string(text, k))