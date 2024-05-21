def main():
    word = input("camelCase: ").strip()
    print(f"snakecase: {snakecase(word)}")

def snakecase(word):
    new_word = ""
    for l in word:
        if l.isupper():
            split_word = word.partition(l)
            print(split_word)
            # To lower case
            split_word_lower = split_word[1].lower()
            # Put the word back together inserting "_"
            new_word = new_word + split_word_lower + "_" + split_word[1]

    return new_word



main()