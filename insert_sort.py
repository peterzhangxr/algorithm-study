# 插入排序
# 比较前面的元素的大小进行插入交换
# 时间复杂度 O(N^2)
# 空间复杂度 O(1)
arr = [3, 1, 2, 9, 4, 3]


def insert_sort():
    for i in range(1, len(arr)):
        for j in reversed(range(i)):
            if arr[j] > arr[j + 1]:
                swap(j, j + 1)


def swap(i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


insert_sort()
print(arr)
