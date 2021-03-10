num1 = float(input("Enter in your first number: "))
num2 = float(input("Enter in your second number: "))
operator = input("Enter in a operator: ")

if (operator == "+"):
    print("The sum between the nums is " + str(num1 + num2))
elif (operator == "-"):
    print("The diffrence between the nums is " + str(num1 - num2))
elif (operator == "*"):
    print("The product between the nums is " + str(num1 * num2))
elif (operator == "/"):
    print("The quotient between the nums is " + str(num1 / num2))
elif (operator == "%"):
    print("The remainder of operation is " + str(num1 % num2))
else:
    print("invalid operator")

