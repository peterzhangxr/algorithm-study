# 位运算学习
arr = [1, 2]
arr[0] = arr[0] ^ arr[1]
arr[1] = arr[0] ^ arr[1]
arr[0] = arr[0] ^ arr[1]
print(arr)

# 取出一个数右边是1的数
eor = 28
eor = eor & (~eor + 1)
print(bin(eor))
