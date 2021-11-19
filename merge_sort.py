# 归并排序
# 先对左侧进行排序，再对右侧进行排序，然后合并
# 时间复杂度 O(NlogN)
arr = [3, 1, 2, 9, 4, 3]


def merge_sort(l, r):
    if l == r:
        return
    m = l + ((r - l) >> 1)
    merge_sort(l, m)
    merge_sort(m + 1, r)
    merge(m, l, r)


def merge(m, l, r):
    helper = []
    p1 = l
    p2 = m + 1
    while p1 <= m and p2 <= r:
        if arr[p1] <= arr[p2]:
            helper.append(arr[p1])
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


merge_sort(0, len(arr) - 1)
print(arr)
