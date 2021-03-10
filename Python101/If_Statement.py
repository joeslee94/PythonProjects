#isMale = True
#isTall = False

##|| is |/or in python
##&& is &/and in python
##else if is elif
##! is not

#if isMale and isTall:
#    print("You are a male")
#elif isMale and not(isTall):
#    print("You are a short male")
#else:
#    print ("You are a female")

def MaxNum(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    elif num1 == num2 == num3:
        return num1
    else:
        return 0

print(MaxNum(4, 5, 6))
