def main():
    word = input("word: ")
    print(shorten(word))


def shorten(word):
    vowels = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}
    for l in word:
        if l in vowels:
            # Partition on the vowel [1], rejoin string before and after the vowel
            split_word = word.partition(l)
            word = split_word[0] + split_word[2]

    return word


if __name__ == "__main__":
    main()
