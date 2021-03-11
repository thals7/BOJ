# # 1. 연결리스트를 이용하여 직접 큐를 구현하여 해결
import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self,node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def pop(self):
        card = self.head.data
        self.head = self.head.next
        return card

    def move(self):
        myCard = self.pop()
        self.push(Node(myCard))

    def last(self):
        return self.head.data


n = int(sys.stdin.readline())
cards = Queue()
for i in range(1,n+1):
    cards.push(Node(i))

for _ in range(n-1):
    cards.pop()
    cards.move()
print(cards.last())


# 2. collections.deque 라이브러리 이용
import sys
from collections import deque
n = int(sys.stdin.readline())
cards = deque()

for i in range(1,n+1):
    cards.append(i)

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())
print(cards.pop())


# 3. 일정한 규칙을 찾아 큐를 이용하지 않고 해결
import sys
n, m = int(sys.stdin.readline()), 1
# 입력값보다 작은 2의 n제곱 중 가장 큰 수를 구한 뒤 그 둘의 차이에 2를 곱함
while n > m:
    m = 2*m
# while문을 벗어나는 순간 m은 입력값보다 크거나 같은 2의 n제곱수이므로 다시 2로 나눠줘야함
# 입력값이 1이거나 2의 n제곱수인 경우 출력값은 입력값과 같음
print(n if n == m else (n-(m//2))*2)