from sys import stdin, stdout
from collections import deque


class Teque:
    def __init__(self):
        self._teque1 = deque()
        self._teque2 = deque()

    def push_back(self, x):
        self._teque2.append(x)
        if len(self._teque2) > len(self._teque1):
            self._teque1.append((self._teque2.popleft()))

    def push_front(self, x):
        self._teque1.appendleft(x)
        if len(self._teque1) > len(self._teque2):
            self._teque2.appendleft((self._teque1.pop()))

    def push_middle(self, x):
        if len(self._teque2) > len(self._teque1):
            self._teque1.append(self._teque2.popleft())
        self._teque2.appendleft(x)

    def get(self, i):
        if i >= len(self._teque1):
            return self._teque2[i - len(self._teque1)]
        return self._teque1[i]


teque = Teque()
for i in range(int(stdin.readline())):
    l = stdin.readline().split()
    if l[0] == 'push_back':
        teque.push_back(int(l[1]))

    elif l[0] == 'push_front':
        teque.push_front(int(l[1]))

    elif l[0] == 'push_middle':
        teque.push_middle(int(l[1]))
    else:
        stdout.write(str(teque.get(int(l[1]))) + '\n')
