import sys


def main():
    # Ensure correct arg count
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if file_is_py(sys.argv[1]) == False:
            sys.exit("Not a Python file")

    line_count = 0
    try:
        with open(sys.argv[1]) as f:
            for line in f:
                if line.strip() == "":
                    continue
                elif line.lstrip().startswith("#"):
                    continue
                else:
                    line_count += 1

    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        print(line_count)


def file_is_py(arg):
    """Ensure file ends with .py"""
    if "." in arg and arg.rsplit(".", 1)[1] == "py":
        return True
    else:
        return False


if __name__ == "__main__":
    main()
