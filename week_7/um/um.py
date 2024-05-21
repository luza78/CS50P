import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    list_of_um = re.findall(r"(^um,| +um[,\.\?!]+|^um$|^um[,\.\?!]+)", s, re.IGNORECASE)
    count = len(list_of_um)
    return count



if __name__ == "__main__":
    main()
