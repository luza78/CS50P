import sys


def main():
    names = []
    adieu = "Adieu, adieu, to"
    # Infinite prompts until user ends with EOF (ctrl + d)
    while True:
        try:
            input_name = input("Name: ").strip().capitalize()

        # User ends program
        except EOFError:
            # Make pretty
            print()
            print(adieu, end=" ")

            # 1 name
            if len(names) == 1:
                print(names[0])

            # 2 names
            elif len(names) == 2:
                # Concat first name with a space "and"
                names[0] = names[0] + " and"
                for name in names:
                    print(name, end=" ")

            # 3 or more names
            elif len(names) > 2:
                # Prepend last name with "and "
                names[-1] = "and " + names[-1]
                # Print all names in list except the last name
                for i in range(len(names) - 1):
                    print(names[i], end=", ")
                print(names[-1], end="")

            print()
            sys.exit()
        else:
            names.append(input_name)


if __name__ == "__main__":
    main()
