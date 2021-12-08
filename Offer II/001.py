# 整数除法

def divider(a, b):
    if a == -2 ** 31 and b == -1:
        return 2 ** 31 - 1

    negative = 2
    if a > 0:
        negative -= 1
        a = -a

    if b > 0:
        negative -= 1
        b = -b

    result = 0
    while a <= b:
        value = b
        quot = 1
        while value >= -2 ** 30 and a <= 2 * value:
            quot += quot
            value += value

        result += quot
        a -= value

    if negative == 1:
        return -result

    return result


print(divider(15, 2))
