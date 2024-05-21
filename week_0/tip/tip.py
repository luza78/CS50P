def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Splits the input string, at $ take the remainder of string after it
    d = float(d.split("$")[1])
    # Round it to single decimal and return it
    return round(d, 1)


def percent_to_float(p):
    # Splits the input string at % and takes remainder before it
    p = p.split("%")[0]
    # format it correctly and cast it to float
    p = float("0.{}".format(p))
    return p


main()
