def main():
    word = input("camelCase: ").strip()
    print(f"snakecase: {snakecase(word)}")


def snakecase(word):
    new_word = ""

    for l in word:
        if l.isupper():
            # Split word when upper
            split_word = word.partition(l)
            # Put upper char to lower
            split_word_lower = split_word[1].lower()
            # Put the word back together inserting "_"
            new_word = new_word + "_" + split_word_lower
            # Continue to loop over the rest of the letters in word
            word = split_word[2]

        else:
            new_word = new_word + l

    return new_word


main()
