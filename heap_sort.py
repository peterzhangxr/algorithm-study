# 堆排序
# 时间复杂度 O(NlogN)
# 额外空间复杂度 O(1)
# 堆是一个完全二叉树，堆分为大根堆和小根堆，大根堆是指每一颗子树的最大值为头节点的值,小根堆是每一颗子湖的最小值为头节点的值
# i位置的左子树是2i+1,右子树是2i+2, 父节点是(i - 1)/2

arr = [7, 1, 2, 8, 3, 6, 7, 8, 3, 9]


def heap_sort():
    for i in reversed(range(len(arr))):
        # heap_insert(i)
        heapify(i, len(arr))

    heap_size = len(arr)
    swap(0, heap_size - 1)
    heap_size -= 1
    heapify(0, heap_size)
    while heap_size > 0:
        heapify(0, heap_size)
        heap_size -= 1
        swap(0, heap_size)


def heap_insert(i):
    p = round((i - 1) / 2)  # 父元素的位置
    while arr[i] > arr[p]:
        swap(i, p)
        i = p
        p = round((i - 1) / 2)  # 父元素的位置


def heapify(i, heap_size):
    left = 2 * i + 1
    # 判断是否还有子孩子
    while left < heap_size:
        largest = left
        if left + 1 < heap_size and arr[left] < arr[left + 1]:
            largest = left + 1

        if arr[largest] > arr[i]:
            swap(largest, i)
            i = largest
            left = 2 * largest + 1
        else:
            break


def swap(i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


print(arr)
heap_sort()
print(arr)
