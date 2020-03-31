"""
两个栈实现一个队列
"""


class Queue:
    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def push(self, node):
        self.stack_a.append(node)

    def pop(self):
        if not self.stack_b:
            if not self.stack_a:
                return None
            else:
                for i in range(len(self.stack_a)):
                    self.stack_b.append(self.stack_a.pop())
        return self.stack_b.pop()


def test_queue():
    times = 5
    test_list = list(range(times))
    queue = Queue()
    for i in range(times):
        queue.push(test_list[i])
    print(test_list)
    for i in range(times):
        print(queue.pop(), end=' ')


test_queue()
