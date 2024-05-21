import emoji


def main():
    user_input = input("Input: ").strip()
    print(emoji.emojize(user_input))


if __name__ == "__main__":
    main()
