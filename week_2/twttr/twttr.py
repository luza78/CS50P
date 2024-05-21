def main():
    # Create a set of vowels we want to remove
    vowels = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}

    user_input = input("Input: ")

    # Print out new word, calling the function to remove vowels
    print(f"Output: {remove_vowels(user_input, vowels)}")


def remove_vowels(input, vowels):
    for l in input:
        if l in vowels:
            # Partition on the vowel [1], rejoin string before and after the vowel
            split_input = input.partition(l)
            input = split_input[0] + split_input[2]

    return input

main()