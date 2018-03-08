# coding=utf-8
"""
@version: 2018/3/8 008
@author: Suen
@contact: sunzh95@hotmail.com
@file: binary_tree
@time: 17:24
@note:  ??
"""


class Node(object):
    def __init__(self, key, lchild=None, rchild=None):
        self.key = key
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree(object):
    def __init__(self, item):
        self.root = Node(item)

    def add(self, item):
        node = Node(item)

        pre_list = [self.root]
        while True:
            root = pre_list.pop(0)
            if root.lchild is None:
                root.lchild = node
                break
            elif root.rchild is None:
                root.rchild = node
                break
            else:
                pre_list.append(root.lchild)
                pre_list.append(root.rchild)

    def traverse(self):
        """
        层次遍历
        :return: 
        """
        print(self.root.key)
        traverse_list = [self.root]
        while traverse_list:
            root = traverse_list.pop(0)
            if root.lchild is not None:
                print(root.lchild.key)
                traverse_list.append(root.lchild)
            if root.rchild is not None:
                print(root.rchild.key)
                traverse_list.append(root.rchild)


if __name__ == '__main__':
    bt = BinaryTree(0)
    bt.add(1)
    bt.add(2)
    bt.add(3)
    bt.add(4)
    bt.traverse()
