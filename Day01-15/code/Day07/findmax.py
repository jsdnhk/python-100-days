"""
找出列表中最大或最小的元素

Version: 0.1
Author: 駱昊
Date: 2018-03-06
"""


def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya']
    # 直接使用內置的max和min函數找出列表中最大和最小元素
    # print(max(fruits))
    # print(min(fruits))
    max_value = min_value = fruits[0]
    for index in range(1, len(fruits)):
        if fruits[index] > max_value:
            max_value = fruits[index]
        elif fruits[index] < min_value:
            min_value = fruits[index]
    print('Max:', max_value)
    print('Min:', min_value)


if __name__ == '__main__':
    main()
# 想一想如果最大的元素有兩個要找出第二大的又該怎麼做 
