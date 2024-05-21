amount_due = 50

# While still due
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    amount_inserted = int(input("Insert Coin: "))

    if amount_inserted in (5, 10, 25):
        amount_due = amount_due - amount_inserted

# Once we break out of the loop, calculate change owed
change_owed = 0 - amount_due
print(f"Change Owed: {change_owed}")
