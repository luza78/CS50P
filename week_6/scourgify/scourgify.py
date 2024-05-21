import sys
import csv


def main():
    # Check for correct amount of command-line arguments
    if len(sys.argv) != 3:
        sys.exit(
            "Incorrect amount of command-line arguments. Usage: python scourgify.py [INPUT FILE] [OUTPUT FILE]"
        )

    # Initialise empty lists to read dicts into
    students_input = []
    students_output = []

    # Open input file and read data
    try:
        with open(sys.argv[1]) as f:
            reader = csv.DictReader(f)
            for student in reader:
                students_input.append(student)
    except FileNotFoundError:
        sys.exit("Input file not found")
    else:
        # Split first, last, strip and add first, last, house into new list of dicts
        for student in students_input:
            students_out = dict()
            students_out["first"] = student["name"].split(",")[1]
            students_out["first"] = students_out["first"].strip()
            students_out["last"] = student["name"].split(",")[0]
            students_out["last"] = students_out["last"].strip()
            students_out["house"] = student["house"]
            students_output.append(students_out)

    # Write to output file
    with open(sys.argv[2], "w") as f:
        headers = ("first", "last", "house")
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(students_output)


if __name__ == "__main__":
    main()
