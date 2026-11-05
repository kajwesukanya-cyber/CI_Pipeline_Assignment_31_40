
def count_words(text):
    return len(text.split())


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print("Word count:", count_words(sentence))
