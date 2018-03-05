# coding=utf-8
"""
@version: 2018/3/5 005
@author: Suen
@contact: sunzh95@hotmail.com
@file: sorting
@time: 15:52
@note:  python 实现排序算法
"""
from daily.clockdeco import clock


@clock
def bubble(list):
    """
    冒泡排序, T(n)=O(n^2), 每次遍历都选出最小的放到i处
    :param list: 
    :return: 
    """
    length = len(list)
    for i in range(length - 1):
        exchange = False  # 如果已经排好序, 就提前返回
        for j in range(i + 1, length):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
                exchange = True
        if exchange == False:
            return list
    return list


@clock
def select_sorting(list):
    """
    选择排序, T(n)=O(n^2), 和冒泡排序类似, 显示的选择出最小的元素, 减少了列表的值交换过程
    :param list: 
    :return: 
    """
    length = len(list)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if list[min_index] > list[j]:
                min_index = j
        if min_index == i:
            return list
        list[i], list[min_index] = list[min_index], list[i]
    return list


@clock
def insertion_sorting(list):
    """
    插入排序, T(n)=O(n^2), 分为有序部分, 无序部分来排序
    :param list: 
    :return: 
    """
    length = len(list)
    for i in range(1, length):
        exchange_index = i  # 未排序部分的元素
        for j in range(i - 1, -1, -1):  # 逆序遍历已排序部分
            if list[exchange_index] < list[j]:
                # 找到第一个比待排序元素小的元素,交换
                list[exchange_index], list[j] = list[j], list[exchange_index]
    return list


@clock
def quick_sorting(list):
    """
    快速排序, T(n)=[O(nlgn), O(n^2)], 从两端向中间同时遍历, 递归
    :param list: 
    :return: 
    """

    def partition(list, left=0, right=len(list) - 1):
        temp = list[left]
        while left < right:
            while left < right and temp < list[right]:
                # 右边值较小时, temp不动, 左移right
                right -= 1
            list[left] = list[right]  # 否则移动到左边
            while left < right and temp > list[left]:
                # 左边值较小时,temp不动, 右移left
                left += 1
            list[right] = list[left]
        list[left] = temp
        return left

    def sub_quick_sorting(list, left=0, right=len(list) - 1):
        if left < right:
            mid = partition(list, left, right)
            sub_quick_sorting(list, left, mid - 1)
            sub_quick_sorting(list, mid + 1, right)

    sub_quick_sorting(list)
    return list


@clock
def heap_sorting(list):
    """
    堆排序, 完全二叉树排序, T(n)=O(nlgn)
    :param list: 
    :return: 
    """

    def adjust_map_heap(list, i, size):
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        max_index = i
        if i < size / 2:
            if lchild < size and list[lchild] > list[max_index]:
                max_index = lchild
            if rchild < size and list[rchild] > list[max_index]:
                max_index = rchild
            if max_index != i:
                list[max_index], list[i] = list[i], list[max_index]
                adjust_map_heap(list, max_index, size)

    def build_map_heap(list, size):
        for i in range((size // 2) - 1, -1, -1):
            adjust_map_heap(list, i, size)

    size = len(list)
    build_map_heap(list, size)
    for i in range(size - 1, -1, -1):
        list[i], list[0] = list[0], list[i]
        adjust_map_heap(list, 0, i)
    return list


if __name__ == '__main__':
    l = [i for i in range(500, 0, -1)]
    # bubble(l)
    # select_sorting(l)
    # insertion_sorting(l)
    # quick_sorting(l)
    heap_sorting(l)
