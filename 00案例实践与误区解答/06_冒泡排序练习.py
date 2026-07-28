



def bubble_sort(my_list):
    n = len(my_list)
    last_index = n - 1
    for i in range(n - 1):
        count = 0
        for j in range(last_index):
            if my_list[j] > my_list[j + 1]:  #  2>1
                count += 1
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                last_index = j
        print(f"第{i+1}轮排序了{count}次")
        if count == 0:
            break




if __name__ == "__main__":
    my_list = [2,5,4,1,6,7,8]
    bubble_sort(my_list)
    print(my_list)