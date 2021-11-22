# 快速排序
# 荷兰国旗问题
# 问题一: 给定一个数组，和一个数num，把小于等于num的数放在数组的左边，大于num的放在数组的右边，要求时间复杂度O(N),额外空间复杂度O(1)
# 定义一个左指针l，开始遍历数组
# 1) 如果arr[i] 小于等于num 左指针l向右移动 与i位置的数交换
# 2) 如果arr[i] 大于num,不做处理，i下移
# 问题二: 给定一个数组，和一个数num，把小于num的数放在数组的左边，等于num的放在右边，大于num的放在数组的右边，要求时间复杂度O(N),额外空间复杂度O(1)
# 定义一个左指针l,再定义一个右指针r，开始遍历数组
# 1) 如果arr[i]大于num 右指针前移，与i位置交换 i不变
# 2) 如果arr[i] 等于num 不做处理 i下移
# 3) 如果arr[i]小于num 左指针右移 与i位置交换 i++
# 当i与右边界相撞时，结束
# 快速排序1.0 取右边的数作为num运用问题一
# 快速排序2.0 取右边的数作为num运用问题二
# 快速排序3.0 随机选一个数作为num运用问题二
# 时间复杂度 O(NlogN)
# 额外空间复杂度O(logN)
import random

arr = [7, 5, 3, 1, 6, 3, 2, 1, 8, 9, 5]


def quick_sort(l, r):
    if l < r:
        num = random.choice(arr)
        t = process(num, l, r)
        quick_sort(l, t[0])
        quick_sort(t[1], r)


def process(num, left, right):
    l = left - 1
    i = left
    r = right + 1
    while i <= (r - 1):
        if arr[i] < num:
            l += 1
            swap(i, l)
            i += 1
        elif arr[i] > num:
            r -= 1
            swap(i, r)
        else:
            i += 1

    return l, r


def swap(i, j):
    if i == j:
        return
    # tmp = arr[i]
    # arr[i] = arr[j]
    # arr[j] = tmp
    arr[i] = arr[i] ^ arr[j]
    arr[j] = arr[i] ^ arr[j]
    arr[i] = arr[i] ^ arr[j]


quick_sort(0, len(arr) - 1)
print(arr)
