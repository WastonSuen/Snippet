# coding=utf-8
"""
@version: 2018/3/7 007
@author: Suen
@contact: sunzh95@hotmail.com
@file: stack_and_queue
@time: 11:38
@note:  

栈是一种运算受限制的链表, 也有共享栈等, FILO

队列也是运算受限的线性表, 也有双端队列, FIFO
双端队列比队列每个节点多储存了 _prev, 代表了前一个节点
"""


class Node(object):
    def __init__(self, value, pnext=None):
        self.value = value
        self._next = pnext


class Stack(object):
    def __init__(self, head=None):
        if head:
            self.head = head
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

    def pop(self):
        if not self.head:
            return None
        else:
            current_node = self.head
            for _ in range(self.length - 2):
                current_node = current_node._next
            value = current_node._next.value
            current_node._next = None
            self.length -= 1
            return value

    def __repr__(self):
        values = []
        current_node = self.head
        while current_node:
            values.append(current_node.value)
            current_node = current_node._next
        return str(values)


class Queue(Stack):
    def popleft(self):
        if not self.head:
            return None
        else:
            current_node = self.head
            self.head = current_node._next
            value = current_node.value
            del current_node
            return value

    def pop(self):
        raise ValueError('Queue not allow this method, use "popleft"')


if __name__ == '__main__':
    print('Stack:')
    stack = Stack()
    stack.push(Node(1))
    stack.push(Node(2))
    print(stack)
    print(stack.pop())
    print(stack)

    print('\nQueue:')
    queue = Queue()
    queue.push(Node(1))
    queue.push(Node(2))
    print(queue)
    print(queue.popleft())
    print(queue)
