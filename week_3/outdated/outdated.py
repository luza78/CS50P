def main():
    months = [
    ("January", "01"),
    ("February", "02"),
    ("March", "03"),
    ("April", "04"),
    ("May", "05"),
    ("June", "06"),
    ("July", "07"),
    ("August", "08"),
    ("September", "09"),
    ("October", "10"),
    ("November", "11"),
    ("December", "12"),
]

    format_date(months)


def format_date(months):
    while True:
        date = input("Date: ").strip()
        # If numeric input
        if "/" in date:
                try:
                    split_date = date.split("/")

                    # If month is only 1 char add leading zero
                    if int(len(split_date[0]) > 2) or int(split_date[0]) > 12 or int(split_date[1]) > 31:
                        continue
                    elif int(len(split_date[0]) < 2):
                        split_date[0] = "0" + split_date[0]

                    # If day is only 1 char, add leading zero
                    if len(split_date[1]) == 1:
                        split_date[1] = "0" + split_date[1]
                except (ValueError, IndexError):
                    continue
                else:
                    formatted_date = split_date[2] + "-" + split_date[0] + "-" + split_date[1]
                    print(formatted_date)
                    break
        # if e.g September 8, 1636
        else:
            try:
                split_date = date.split(" ")
                # Validate input: Not shorter than 3, has a ',' not shorter than 2, no day over 31
                if not len(split_date[0]) < 3 and "," in split_date[1] and not len(split_date[1]) < 2 and not int(split_date[1].split(",")[0]) > 31:
                    split_date[1] = "0" + split_date[1][0]
                else:
                    continue

                if int(len(split_date[1]) > 2):
                    continue
            # Catches the likely errors from input
            except (IndexError, ValueError):
                continue
            else:
                month = split_date[0].capitalize()
                # Iterate over the list of months (tuples) finding the matching month and numeric value
                for m, numeric in months:
                    if month == m:
                        formatted_date = split_date[2] + "-" + str(numeric) + "-" + split_date[1]
                        print(formatted_date)
                # Break out of while Loop regardless of outcome
                break


main()
