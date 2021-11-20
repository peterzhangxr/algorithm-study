# 小和问题
# 在一个数组中每一个数左边比当前数小的数累加起来，叫做这个数组的小和
# 转换为求一个数右边比这个数大的数的小和
# 同理还有逆序对问题
# 时间复杂度 O(NlogN)
arr = [1, 3, 4, 2, 5]


def merge_sort(l, r):
    if l == r:
        return 0
    m = l + ((r - l) >> 1)
    a = merge_sort(l, m)
    b = merge_sort(m + 1, r)
    c = merge(m, l, r)
    return a + b + c


def merge(m, l, r):
    helper = []
    p1 = l
    p2 = m + 1
    total = 0
    while p1 <= m and p2 <= r:
        if arr[p1] < arr[p2]:
            helper.append(arr[p1])
            total += (r - p2 + 1) * arr[p1]
            p1 += 1
        else:
            helper.append(arr[p2])
            p2 += 1

    while p1 <= m:
        helper.append(arr[p1])
        p1 += 1

    while p2 <= r:
        helper.append(arr[p2])
        p2 += 1

    for k in range(len(helper)):
        arr[l + k] = helper[k]

    return total


print(merge_sort(0, len(arr) - 1))
print(arr)
