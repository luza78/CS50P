def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    amount_due = 0
    while True:
        amount_due = get_order(amount_due, menu)
        try:
            print(f"Total: ${amount_due:.2f}")
        except TypeError:
            pass


def get_order(previous_total, menu):
    while True:
        try:
            item = input("Item: ").title()
        except EOFError:
            exit()
        else:
            if item in menu:
                return float(menu[item]) + previous_total
            else:
                continue


main()
