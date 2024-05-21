def main():
    get_groceries()


def get_groceries():
    # Create empty dict
    groceries = {}

    while True:
        try:
            item = input().upper()
        except EOFError:
            # When ctrl+ d, groceries.items returns a list of tuples, sorted sorts them, and dict() turns it back into a dict
            groceries = dict(sorted(groceries.items()))
            for i in groceries:
                print(f"{groceries[i]} {i}")
            exit()
        else:
            # If in list, add 1 to value
            if item in groceries:
                groceries[item] += 1
            else:
                # If not in list, initialise it to a value of 1
                groceries[item] = 1


main()
