
def first_non_repeating(text):
    for char in text:
        if text.count(char) == 1:
            return char

    return None


if __name__ == "__main__":
    text = input("Enter a string: ")
    result = first_non_repeating(text)
    print("First non-repeating character:", result)
