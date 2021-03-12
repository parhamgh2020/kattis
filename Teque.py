from math import ceil
from sys import stdin, stdout
from collections import deque

class Teque():
    def __init__(self):
        self.memory = deque()

    def __len__(self):
        return len(self.memory)

    def push_back(self, x):
        self.memory.append(x)

    def push_front(self, x):
        self.memory.appendleft(x)

    def push_middle(self, x):
        self.memory.insert(ceil(len(self) / 2), x)

    def get(self, x):
        print(self.memory[x])


input()
instance = Teque()
while True:
    try:
        a, b = input().split()
        eval(f'instance.{a}({b})')
    except EOFError:
        break

# teque = Teque()
# for i in range(int(stdin.readline())):
#     l = stdin.readline().split()
#     if l[0] == 'push_back':
#         teque.push_back(int(l[1]))
#
#     elif l[0] == 'push_front':
#         teque.push_front(int(l[1]))
#
#     elif l[0] == 'push_middle':
#         teque.push_middle(int(l[1]))
#     else:
#         stdout.write(str(teque.get(int(l[1]))) + '\n')

