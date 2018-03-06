# coding=utf-8
"""
@version: 2018/3/6
@author: Suen
@contact: sunzh95@hotmail.com
@file: linked_list
@time: 23:34
@note:  ??
"""


class Node(object):
    def __init__(self, value, pnext=None):
        self.value = value
        self._next = pnext


class LinkedList(object):
    def __init__(self, node):
        if isinstance(node, Node):
            self.head = node
            self.length = 1
        else:
            self.head = None
            self.length = 0

    def append(self, node):
        item = node if isinstance(node, Node) else Node(node)
        if not self.head:
            self.head = item
        else:
            current_node = self.head
            while current_node._next:
                current_node = current_node._next
            current_node._next = item
        self.length += 1
        return True

    def pop(self):
        current_node = self.head
        for _ in range(self.length - 2):
            current_node = current_node._next

        value = current_node._next.value
        del current_node._next
        current_node._next = None
        self.length -= 1
        return value

    def insert(self, k, node):
        item = node if isinstance(node, Node) else Node(node)
        if not self.head or k == self.length:
            return self.append(item)
        if k > self.length:
            raise ValueError('index out of range')

        current_node = self.head
        if k == 0:
            item._next = current_node
            self.head = item
        elif 0 < k and k <= self.length - 1:
            for _ in range(k - 1):
                current_node = current_node._next
            item._next = current_node._next
            current_node._next = item
        self.length += 1
        return True

    def remove(self, k):
        if not self.head:
            print('linked list is already empty')
            return True
        if k > self.length - 1:
            raise ValueError('index out of range')
        if k == self.length - 1:
            return self.pop()

        current_node = self.head
        if k == 0:
            self.head = current_node._next
        elif 0 < k and k < self.length - 1:
            for _ in range(k - 1):
                current_node = current_node._next
            current_node._next = current_node._next._next
        value = current_node.value
        del current_node
        self.length -= 1
        return value

    def update(self, k, node):
        item = node if isinstance(node, Node) else Node(node)
        if not self.head:
            self.append(item)
        if k == self.length - 1:
            self.pop()
            self.append(item)
        if k == 0:
            item._next = self.head._next
            del self.head._next
            self.head = item
        elif 0 < k and k < self.length - 1:
            curreent_node = self.head
            for _ in range(k - 1):
                curreent_node = curreent_node._next
            item._next = curreent_node._next._next
            del curreent_node._next
            curreent_node._next = item

    def print(self):
        current_node = self.head
        print(current_node.value),
        while current_node._next:
            current_node = current_node._next
            print(current_node.value),


if __name__ == '__main__':
    linked_list = LinkedList(Node(0))
    linked_list.append(Node(1))
    linked_list.append(Node(2))
    linked_list.append(3)
    linked_list.pop()
    linked_list.update(1, 4)
    linked_list.remove(0)
    linked_list.insert(0, 5)
    linked_list.print()
