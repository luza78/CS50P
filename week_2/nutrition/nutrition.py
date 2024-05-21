# Create a dict of fruits
fruits = {
    "apple": 130, "avocado": 50,
    "banana": 110, "cantaloupe": 50,
    "grapefruit": 60, "grapes": 90,
    "honeydew": 50, "kiwifruit": 90,
    "lemon": 15, "lime": 20,
    "nectarine": 60, "orange": 80,
    "peach": 60, "pear": 100,
    "pineapple": 50, "plums": 70,
    "strawberries": 50, "sweet cherries": 100,
    "tangerine": 50, "watermelon": 80
}

which_fruit = input("Choose fruit: ").lower()

# If the fruit is in our dictionary, print the value from the key
if which_fruit in fruits:
    print(f"Calories: {fruits[which_fruit]}")