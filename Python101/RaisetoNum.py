def exponent(basenum, pownum):
    result = 1
    for index in range(pownum):
        result *= basenum
    return result

print(exponent(5, 4))