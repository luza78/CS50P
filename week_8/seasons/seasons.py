from datetime import date
import re
import sys
import inflect


def main():
    # Get user date of birth
    dob = input("Date of birth: ")

    # Validate and return the captured groups
    dob = validate_date(dob)
    # Make dob a date object
    dob = date(int(dob[0]), int(dob[1]), int(dob[2]))
    # Get todays date
    date_today = date.today()
    # Overload the - operator, returning a time delta object
    delta = date_today - dob
    # Get total seconds of time delta divide by 60 to convert to minutes
    minutes = round(delta.total_seconds() / 60)

    # Init p as an inflect object
    p = inflect.engine()
    # Change number to words using the number_to_words method, passing in the time delta in minutes
    # Capitalizing, and removing "and" and the leading space, replacing it with ""
    result = p.number_to_words(minutes).capitalize().replace(" and", "")
    # Print result, adding "minutes" to the end
    print(result, "minutes")


def validate_date(dob):
    # Validate input format
    valid_dob = re.search(
        r"^(\d\d\d\d)-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$", dob
    )
    if not valid_dob:
        sys.exit("Invalid Date")
    else:
        return valid_dob.groups()


if __name__ == "__main__":
    main()
