def main():
    word = input("Phrase: ")

    print(smiley(word))

def smiley(phrase):
    phrase = phrase.replace(":)", "🙂")
    phrase = phrase.replace(":(", "🙁")
    return phrase

main()