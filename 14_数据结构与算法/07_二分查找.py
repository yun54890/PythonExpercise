


def binary_search(my_list,target):
    # 1 2 3 4 5 6 7
    # s   e m s   e
    start = 0
    end = len(my_list)-1

    while start<=end:
        mid = (start+end)//2
        if my_list[mid]==target:
            return mid
        elif my_list[mid]<target:  # mid=4 < target=7
            start = mid+1
        else:
            end = mid-1
    return -1






if __name__ == '__main__':
    my_list = [1,2,3,4,5,6,7,8,9,10]
    print(binary_search(my_list,11))