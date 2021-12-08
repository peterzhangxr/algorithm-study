# 002 二进制加法
def addBinary(a, b):
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    s = ''
    while i >= 0 or j >= 0:
        if i >= 0:
            charA = int(a[i:i+1])
            i -= 1
        else:
            charA = 0

        if j >= 0:
            charB = int(b[j:j+1])
            j -= 1
        else:
            charB = 0
        sum = charA + charB + carry
        if sum >= 2:
            carry = 1
            sum = sum - 2
        else:
            carry = 0

        s += str(sum)
    if carry > 0:
        s += str(carry)

    return s[::-1]

print(addBinary('111', '10'))