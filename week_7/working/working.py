import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Searches input string, caputring 6 groups. The hour, minutes, and AM or PM
    match = re.search(
        r"([1-9][0-2]?):?([0-5][0-9])? (AM|PM) to ([1-9][0-2]?):?([0-5][0-9])? (AM|PM)",
        s,
        re.IGNORECASE,
    )
    try:
        all_match = match.groups()
    except AttributeError:
        raise ValueError("")
    else:
        # Left hand conversion
        if match.group(3).lower() == "am":
            converted_time_left = ""
            # Hours AM
            if match.group(1) == "12":
                converted_time_left = "00"
            elif match.group(1) == "11" or match.group(1) == "10":
                converted_time_left = match.group(1)
            else:
                converted_time_left = "0" + match.group(1)

        elif match.group(3).lower() == "pm":
            converted_time_left = ""
            # Hours PM
            if match.group(1) == "12":
                converted_time_left = match.group(1)
            elif match.group(1) == "1":
                converted_time_left = "13"
            elif match.group(1) == "2":
                converted_time_left = "14"
            elif match.group(1) == "3":
                converted_time_left = "15"
            elif match.group(1) == "4":
                converted_time_left = "16"
            elif match.group(1) == "5":
                converted_time_left = "17"
            elif match.group(1) == "6":
                converted_time_left = "18"
            elif match.group(1) == "7":
                converted_time_left = "19"
            elif match.group(1) == "8":
                converted_time_left = "20"
            elif match.group(1) == "9":
                converted_time_left = "21"
            elif match.group(1) == "10":
                converted_time_left = "22"
            elif match.group(1) == "11":
                converted_time_left = "23"

        # Minutes
        if match.group(2):
            converted_time_left = converted_time_left + ":" + match.group(2)
        else:
            converted_time_left = converted_time_left + ":00"

        # Right hand conversion
        if match.group(6).lower() == "am":
            converted_time_right = ""
            # Hours AM
            if match.group(4) == "12":
                converted_time_right = "00"
            elif match.group(4) == "11" or match.group(1) == "10":
                converted_time_right = match.group(1)
            else:
                converted_time_right = "0" + match.group(1)

        elif match.group(6).lower() == "pm":
            converted_time_right = ""
            # Hours PM
            if match.group(4) == "12":
                converted_time_right = match.group(1)
            elif match.group(4) == "1":
                converted_time_right = "13"
            elif match.group(4) == "2":
                converted_time_right = "14"
            elif match.group(4) == "3":
                converted_time_right = "15"
            elif match.group(4) == "4":
                converted_time_right = "16"
            elif match.group(4) == "5":
                converted_time_right = "17"
            elif match.group(4) == "6":
                converted_time_right = "18"
            elif match.group(4) == "7":
                converted_time_right = "19"
            elif match.group(4) == "8":
                converted_time_right = "20"
            elif match.group(4) == "9":
                converted_time_right = "21"
            elif match.group(4) == "10":
                converted_time_right = "22"
            elif match.group(4) == "11":
                converted_time_right = "23"

        # Minutes
        if match.group(5):
            converted_time_right = converted_time_right + ":" + match.group(5)
        else:
            converted_time_right = converted_time_right + ":00"

        # Finally join the converted times together, and return
        converted_time = converted_time_left + " to " + converted_time_right
        return converted_time


if __name__ == "__main__":
    main()
