# 冒泡排序
# 比较相邻的两个元素的大小进行交换
# 时间复杂度 O(N^2)
# 空间复杂度 O(1)
arr = [3, 1, 2, 9, 4, 3]


def bubble_sort():
    for i in reversed(range(len(arr))):
        for j in range(i):
            if arr[j] > arr[j+1]:
                swap(j, j+1)


def swap(i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

bubble_sort()
print(arr)
