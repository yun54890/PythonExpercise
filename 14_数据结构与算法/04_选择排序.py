








def select_sort(my_list):
    n = len(my_list)
    for i in range(n - 1):
        min_index = i
        for j in range(i+1,n):
            if my_list[min_index] > my_list[j]:
                min_index = j
        if min_index != i:
            my_list[min_index], my_list[i] = my_list[i], my_list[min_index]




if __name__ == '__main__':
    my_list = [8,5,1,0,2,9,3,8,5,-3,0,9,1,4]
    select_sort(my_list)
    print(my_list)