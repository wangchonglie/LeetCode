"""
两个队列实现一个栈
"""
from collections import deque


class Stack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, node):
        self.queue1.append(node)

    def pop(self):
        if len(self.queue1) == 0:
            return None
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.popleft())
        # 交换是为了下一次的pop
        self.queue1, self.queue2 = self.queue2, self.queue1
        return self.queue2.pop()


def test_stack():
    times = 10
    test_list = list(range(times))
    stack = Stack()
    for i in range(times):
        stack.push(test_list[i])
    print(test_list)
    for i in range(times):
        print(stack.pop(), end=' ')


test_stack()
