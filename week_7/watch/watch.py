import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Looks for the src, grouping the unique embed id
    match = re.search(r".*src=\"http(?:s)?\://(?:www\.)?youtube\.com/embed/(\w+)\"", s, re.IGNORECASE)
    # If it matches
    if match:
        # Store the embed id in variable, concat with the url
        video_code = match.groups(1)
        url = "https://youtu.be/" + video_code[0]
        return url


if __name__ == "__main__":
    main()
