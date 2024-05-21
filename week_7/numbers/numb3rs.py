import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    #Split over multiple lines to improve readability
    if re.search(
        r"^((2[0-5][0-5])|(2[0-4][0-9])|(1[0-9][0-9])|([1-9][0-9])|[0-9])\."
        r"((2[0-5][0-5])|(2[0-4][0-9])|(1[0-9][0-9])|([1-9][0-9])|[0-9])\."
        r"((2[0-5][0-5])|(2[0-4][0-9])|(1[0-9][0-9])|([1-9][0-9])|[0-9])\."
        r"((2[0-5][0-5])|(2[0-4][0-9])|(1[0-9][0-9])|([1-9][0-9])|[0-9])$",
        ip
    ):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
