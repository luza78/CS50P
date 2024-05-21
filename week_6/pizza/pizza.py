import sys
import csv
from tabulate import tabulate


def main():
    # Ensure correct arg count
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        # Ensure CSV
        if file_is_csv(sys.argv[1]) == False:
            sys.exit("Not a CSV file")

    menu = []
    try:
        with open(sys.argv[1]) as f:
            reader = csv.DictReader(f)
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        print(tabulate(menu, headers="keys", tablefmt="grid"))


def file_is_csv(arg):
    """Ensure file ends with .py"""
    if "." in arg and arg.rsplit(".", 1)[1] == "csv":
        return True
    else:
        return False


if __name__ == "__main__":
    main()
