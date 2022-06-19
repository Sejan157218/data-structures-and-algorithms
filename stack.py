from collections import deque


class stack:
    def __init__(self):
        self.container=deque();

    def push(self,value):
        self.container.append(value)
    def pop(self):
        self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0;
    def size(self):
        return len(self.container);


if __name__ == '__main__':
    s=stack()
    print(s.push(4))
    print(s.push(4))
    print(s.push(5))
    print(s.push(5))
    print(s.pop())
    print(s.size())
    print(s.is_empty())
    print(s.peek())



    