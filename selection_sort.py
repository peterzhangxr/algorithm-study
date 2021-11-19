# 选择排序
# 先假设给定列表第一个是最小(最大元素)
# 向后遍历比较，进行交换
# 时间复杂度 O(N^2)
# 空间复杂度 O(1)
arr = [3, 1, 2, 9, 4]


def selection_sort():
    if len(arr) < 2:
        print('列表的长度必须大于2')
    else:

        for i in range(len(arr)):
            min_index = i
            for j in range(i, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            if min_index != i:
                swap(i, min_index)


def swap(i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    # arr[i] = arr[i] ^ arr[j]
    # arr[j] = arr[i] ^ arr[j]
    # arr[i] = arr[i] ^ arr[j]


selection_sort()
print(arr)
