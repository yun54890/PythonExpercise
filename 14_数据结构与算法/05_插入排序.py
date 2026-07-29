


def insert_sort(my_list):
    n = len(my_list)
    for i in range(1,n):
        for j in range(i,0,-1):
            if my_list[j] < my_list[j-1]:   # 3 > 2
                my_list[j],my_list[j-1] = my_list[j-1],my_list[j]
            else:
                break




if __name__=='__main__':
    my_list = [8,9,0,2,8,3,4,0,9,5,8,2,3,4]
    insert_sort(my_list)
    print(my_list)