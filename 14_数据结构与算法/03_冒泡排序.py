"""
案例：演示冒泡排序

冒泡排序介绍：
    原理：
        相邻元素两两比较,大的往后走,这样第一轮比较完毕之后，最大值就在最大索引处.
        重复此动作，直至排序完成
    流程：假设有五个元素
        第几轮(索引)              该轮比较的总次数             公式
         第1轮(0)                     4次                5 - 1 - 0 = 4
         第2轮(1)                     3次                5 - 1 - 1 = 3
         第3轮(2)                     2次                5 - 1 - 2 = 2
         第4轮(3)                     1次                5 - 1 - 3 = 1
    要点:
        1. 比较的总论数               列表长度 - 1
        2. 每轮比较的总次数            列表长度 - 1 - 轮数的索引(从0开始)
        3. 谁和谁比较                 索引j 和 j+1位置的元素比较
"""



def bubble_sort(my_list):
    # last_index = len(my_list)-1
    n = len(my_list)
    for i in range(n - 1):
        count = 0
        for j in range(n-1-i):
            if my_list[j] > my_list[j + 1]:
                count += 1
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                # last_index = j
        print(f"第{i+1}轮交换了{count}次")

        if count == 0:
            break



if __name__ == "__main__":
    my_list = [7,1,3,6,8,9,10]
    # my_list = [1,2,3,4,5,6,7,8,9]
    bubble_sort(my_list)
    print(my_list)