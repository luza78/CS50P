from PIL import Image, ImageOps
import sys


def main():
    # Check amount of command-line arguments
    if len(sys.argv) != 3:
        sys.exit(
            "Incorrect amount of command-line arguments. Usage: python shirt.py [INPUT FILE] [OUTPUT FILE]"
        )

    # Validate file extensions
    if not file_extension(sys.argv[1], sys.argv[2]):
        sys.exit("Unsupported file extension. must be .jpg .jpeg .png")

    # Verify input and output extensions match
    if not file_extension_match(sys.argv[1], sys.argv[2]):
        sys.exit("Input and output file extensions do not match")

    # Open to read files
    try:
        shirt = Image.open("shirt.png")
        before = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Error, file does not exist")
    # Write files to new variable
    size = shirt.size
    before_cropped = ImageOps.fit(before, size)
    before_cropped.paste(shirt, shirt)
    # 'Save' file, writing it to disk
    before_cropped.save(sys.argv[2])


# Verify valid extensions
def file_extension(arg1, arg2):
    ext = {"jpg", "jpeg", "png"}
    if not "." in arg1 or arg1.lower().rsplit(".", 1)[1] not in ext:
        return False
    elif not "." in arg2 or arg2.lower().rsplit(".", 1)[1] not in ext:
        return False
    else:
        return True


# Verify extensions match
def file_extension_match(arg1, arg2):
    if not arg1.lower().rsplit(".", 1)[1] == arg2.lower().rsplit(".", 1)[1]:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
