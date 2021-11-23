# 基数排序(桶)
import math

arr = [189, 13, 17, 62, 100, 53, 41]


def cardinal_sort():
    _max = max_bits()
    for d in range(_max):
        count = []
        bucket = []
        # 生命一个数组
        for i in range(10):
            count.append(0)

        # 统计每一位的个数
        for i in range(len(arr)):
            bucket.append(0)
            j = get_digit(arr[i], d)
            count[j] += 1

        # 将个数与前一位相加
        for i in range(1, len(count)):
            count[i] = count[i] + count[i - 1]

        # 从最后一位开始遍历，临时数组塞入桶中
        for i in reversed(range(len(arr))):
            j = get_digit(arr[i], d)
            idx = count[j] - 1
            bucket[idx] = arr[i]
            count[j] -= 1

        # 将桶中的数据依次取出
        for i in range(len(arr)):
            arr[i] = bucket[i]


def max_bits():
    _max = 0
    for i in range(len(arr)):
        if arr[i] > _max:
            _max = arr[i]
    i = 0
    while _max != 0:
        i += 1
        _max = math.floor(_max / 10)
    return i


def get_digit(x, d):
    return math.floor(x / math.pow(10, d)) % 10


print(arr)
cardinal_sort()
print(arr)
