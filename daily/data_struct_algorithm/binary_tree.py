# coding=utf-8
"""
@version: 2018/3/8 008
@author: Suen
@contact: sunzh95@hotmail.com
@file: binary_tree
@time: 17:24
@note:  ??
"""
from daily.data_struct_algorithm.stack_and_queue import Queue, Stack


class BinaryNode(object):
    def __init__(self, key, lchild=None, rchild=None):
        self.key = key
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree(object):
    def __init__(self, item):
        self.root = BinaryNode(item)

    def normal_add(self, item):
        node = BinaryNode(item)

        pre_list = [self.root]
        while True:
            root = pre_list.pop(0)  # 列表取出index为0的元素, 时间复杂度为O(n)
            if root.lchild is None:
                root.lchild = node
                break
            elif root.rchild is None:
                root.rchild = node
                break
            else:
                pre_list.append(root.lchild)
                pre_list.append(root.rchild)

    def normal_traverse(self):
        """
        层次遍历
        :return: 
        """
        traverse_list = [self.root]
        while traverse_list:
            root = traverse_list.pop(0)
            print(root.key)
            if root.lchild is not None:
                traverse_list.append(root.lchild)
            if root.rchild is not None:
                traverse_list.append(root.rchild)

    def add(self, item):
        """
        添加元素, 队列实现
        :param item:
        :return:
        """
        node = BinaryNode(item)
        queue = Queue(self.root)
        while True:
            root = queue.popleft()
            if root.lchild is None:
                root.lchild = node
                break
            elif root.rchild is None:
                root.rchild = node
                break
            else:
                queue.push(root.lchild)
                queue.push(root.rchild)

    def traverse(self):
        """
        层次遍历, 队列实现
        :return:
        """
        traverse_queue = Queue(self.root)
        while traverse_queue.length > 0:
            root = traverse_queue.popleft()
            print(root.key)
            if root.lchild is not None:
                traverse_queue.push(root.lchild)
            if root.rchild is not None:
                traverse_queue.push(root.rchild)

    def pre_traverse(self):
        """
        先序遍历, list实现, 或Stack实现也可
        :return:
        """
        pre_traverse_list = [self.root]
        while pre_traverse_list:
            root = pre_traverse_list.pop()
            print(root.key)
            if root.rchild is not None:
                pre_traverse_list.append(root.rchild)
            if root.lchild is not None:
                pre_traverse_list.append(root.lchild)


if __name__ == '__main__':
    bt = BinaryTree(0)
    bt.add(1)
    bt.add(2)
    bt.add(3)
    bt.add(4)
    bt.traverse()
    bt.pre_traverse()
