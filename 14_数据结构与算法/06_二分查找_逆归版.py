



def binary_search_recursion(my_list,target):
    """
    该函数是二分查找,
    :param my_list:  列表
    :param target:  查找的目标值
    :return:  True 目标值存在  False 目标值不存在
    """
    n = len(my_list)
    if n == 0:
        return -1

    mid = n//2
    if my_list[mid] == target:
        return mid
    elif my_list[mid] < target:      # 1 2 3 4 5    mid=3 < target=5
        return binary_search_recursion(my_list[mid+1:],target)
    else:        # mid=3 > target=2  1 2 3 4 5
        return binary_search_recursion(my_list[:mid],target)

    return -1


if __name__ == '__main__':
    my_list = [1,2,3,4,5,6,7,8,9,10]
    print(binary_search_recursion(my_list,2))