from pyfiglet import Figlet
import sys
import random


def main():
    # Initialize
    f = Figlet()
    # Make empty list
    font_list = []
    # Get fonts, and store them in a list
    fonts = f.getFonts()
    for font in fonts:
        font_list.append(font)

    # If run with no arguements
    if len(sys.argv) < 2:
        # Pass the list to random.choice to pick one at random
        font_choice = random.choice(font_list)
        # Set font
        f = Figlet(font=font_choice)
        # Get input
        phrase = input("Input: ").strip()
        # Print
        print(f.renderText(phrase))

    # If run with 2 arguments. -f or --f and if font in argv[2] is in our fonts
    elif (
        len(sys.argv) == 3
        and sys.argv[1] == "-f"
        or sys.argv[1] == "--font"
        and sys.argv[2] in font_list
    ):
        # Set font to argv[2]
        f = Figlet(font=sys.argv[2])
        phrase = input("Input: ").strip()
        print(f.renderText(phrase))

    # Invalid input
    else:
        sys.exit("Invalid Usage")


if __name__ == "__main__":
    main()
