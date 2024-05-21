def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):

    greeting = greeting.lower()
    # Checks if hello is in first string
    if "hello" in greeting.split()[0]:
        return 0
    # Checks if h is first letter
    elif greeting[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()


