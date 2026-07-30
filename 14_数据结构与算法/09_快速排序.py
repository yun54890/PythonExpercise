def quick_sort(my_list, start, end):
    # 第一步：边界判断！无效区间直接return，不要访问数组
    if start >= end:
        return

    left = start
    right = end
    mid = my_list[start]

    while left < right:
        while my_list[right] >= mid and left < right:
            right -= 1
        my_list[left] = my_list[right]

        while my_list[left] < mid and left < right:
            left += 1
        my_list[right] = my_list[left]
    my_list[left] = mid

    quick_sort(my_list, start, left - 1)
    quick_sort(my_list, left + 1, end)


if __name__ == '__main__':
    my_list = [9, 7, 5, 4, 3, 4, 2, 6, 3, 0, 1]
    quick_sort(my_list, 0, len(my_list) - 1)
    print(my_list)