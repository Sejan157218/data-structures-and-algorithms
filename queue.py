from collections import deque


class Queue:
    def __init__(self):
        self.container=deque();

    def queue(self,value):
        self.container.appendleft(value)
    def pop(self):
        self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0;
    def size(self):
        return len(self.container);


if __name__ == '__main__':
    s = Queue()
    print(s.queue(4))
    print(s.queue(4))
    print(s.queue(5))
    print(s.queue(5))
    print(s.pop())
    print(s)
    print(s.size())
    print(s.is_empty())
    print(s.peek())