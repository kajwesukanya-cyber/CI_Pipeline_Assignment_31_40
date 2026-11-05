def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())


if __name__ == "__main__":
    str1 = input("Enter first word: ")
    str2 = input("Enter second word: ")

    result = is_anagram(str1, str2)
    print("Anagram:", result)