import sys

input = lambda: sys.stdin.readline().rstrip()

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None
        self.stackSize = 0

    def size(self):
        return self.stackSize

    def empty(self):
        if self.head is None:
            return 1
        else:
            return 0

    def push(self,x):
        new = node(x)

        new.next = self.head
        self.head = new
        self.stackSize += 1

    def pop(self):
        if self.empty():
            return -1
        else:
            popData = self.head.data
            self.head = self.head.next
            self.stackSize -= 1

            return popData

    def top(self):
        if self.empty():
            return -1
        else:
            return self.head.data

s = stack()
n = int(input())

for _ in range(n):
    cmd = input()
    if cmd.split()[0] == "push":
        x = cmd.split()[1]
        s.push(int(x))
    elif cmd == "pop":
        print(s.pop())
    elif cmd == "size":
        print(s.size())
    elif cmd == "empty":
        print(s.empty())
    elif cmd == "top":
        print(s.top())