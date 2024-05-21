def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Must start with at least 2 letters
    if not plate[0].isalpha() and plate[1].isalpha():
        # If letter 1 and 2 is not alphabetical
        return False

    # plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if len(plate) > 6:
        return False

    alpha_chars = 0
    num_chars = 0
    # Counts amount of alphabetical and numeric characters in the plate
    for l in plate:
        if l.isalpha():
            alpha_chars += 1
        elif l.isnumeric():
            num_chars += 1

    if alpha_chars < 2:
        return False

    # If plate has numbers
    if num_chars > 0:
        # Check last char is number
        if not plate[-1].isnumeric():
            return False

        # Find first number and check for '0'
        checked_for_0 = False
        for l in plate:
            if l.isnumeric() and not checked_for_0:
                if l == "0":
                    return False
                # if first num is not 0, check remaining chars are numeric
                else:
                    # Sets flag to true, allowing us to break out of the outer loop
                    checked_for_0 = True
                    # Splits plate on the first numer
                    split_plate = plate.split(l)
                    # Checks remaining characters are numeric
                    for remaining in split_plate[1]:
                        if not remaining.isnumeric():
                            return False

    # Validate letters and numbers only
    if not plate.isalnum():
        return False
    else:
        return True


if __name__ == "__main__":
    main()
