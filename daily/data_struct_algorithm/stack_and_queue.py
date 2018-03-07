# coding=utf-8
"""
@version: 2018/3/7 007
@author: Suen
@contact: sunzh95@hotmail.com
@file: stack_and_queue
@time: 11:38
@note:  

栈是一种运算受限制的线性表, 也有共享栈等, FILO, 递归的本质也是栈
push, pop, 都是 T(n)=O(1), 此处是基于数组的实现方式

队列也是运算受限的线性表, 也有双端队列, FIFO, 常用于消息队列
双端队列比队列每个节点多储存了 _prev, 代表了前一个节点
push, pop, 都是 T(n)=O(1), 此处是基于链表的实现方式

"""
from typing import Iterable


class Stack(object):
    def __init__(self, init=None):
        if isinstance(init, Iterable):
            self.items = [v for v in init]
        elif init:
            self.items = [init]
        else:
            self.items = []

    def push(self, item):
        self.items.append(item)

    @property
    def top(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def __repr__(self):
        return str(self.items)


class Node(object):
    def __init__(self, value, pnext=None):
        self.value = value
        self._next = pnext


class Queue(object):
    def __init__(self, node=None):
        if node:
            self.head = node
            self.length = 1
        else:
            self.head = None
            self.length = 0

    def push(self, node):
        if not self.head:
            self.head = node
        else:
            current_node = self.head
            while current_node._next:
                current_node = current_node._next
            current_node._next = node
        self.length += 1
        return True

    def popleft(self):
        if not self.head:
            return None
        else:
            current_node = self.head
            self.head = current_node._next
            value = current_node.value
            del current_node
            self.length -= 1
            return value

    def __repr__(self):
        current_node = self.head
        values = []
        while current_node:
            values.append(current_node.value)
            current_node = current_node._next
        return str(values)


if __name__ == '__main__':
    print('Stack:')
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack)

    print('\nQueue:')
    queue = Queue()
    queue.push(Node(1))
    queue.push(Node(2))
    print(queue)
    print(queue.popleft())
    print(queue)
