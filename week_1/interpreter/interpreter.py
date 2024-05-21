equation = input("Expression: ").strip().split()

if equation[1] == "+":
    print(float(equation[0]) + float(equation[2]))

elif equation[1] == "-":
    print(float(equation[0]) - float(equation[2]))

elif equation[1] == "*":
    print(float(equation[0]) * float(equation[2]))

elif equation[1] == "/":
    print(float(equation[0]) / float(equation[2]))

else:
    print("Usage: x (+, -, *, /) y")
