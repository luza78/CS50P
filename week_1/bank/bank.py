greeting = input("Greeting: ").strip().lower()

# Checks if hello is in first string
if "hello" in greeting.split()[0]:
    print("$0")

# Checks if h is first letter
elif greeting[0] == "h":
    print("$20")

else:
    print("$100")