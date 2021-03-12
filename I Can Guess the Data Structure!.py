class Queue:
    def __init__(self):
        self.q = []

    def queue(self, io, element=None):
        if io == 1:
            self.q.append(element)
        else:
            return self.q.pop(0) if len(self.q) else 'impossible'


class Stack:
    def __init__(self):
        self.s = []

    def stack(self, io, element=None):
        if io == 1:
            self.s.append(element)
        else:
            return self.s.pop() if len(self.s) else 'impossible'


class Heap:
    def __init__(self):
        self.h = []

    def heap(self, io, element=None):
        if io == 1:
            self.h.append(element)
            self.h.sort(reverse=True)
        else:
            return self.h.pop(0) if len(self.h) else 'impossible'


while True:
    try:
        s, q, h = True, True, True
        stack = Stack()
        heap = Heap()
        queue = Queue()
        for _ in range(int(input())):
            io, element = map(int, input().split())
            if io == 1:
                heap.heap(io, element)
                stack.stack(io, element)
                queue.queue(io, element)
            else:
                if h and element != heap.heap(io):
                    h = False
                if s and element != stack.stack(io):
                    s = False
                if q and element != queue.queue(io):
                    q = False
        if sum([s, q, h]) > 1:
            print('not sure')
        elif sum(([s, q, h])) == 0:
            print('impossible')
        elif h:
            print('priority queue')
        elif s:
            print('stack')
        else:
            print('queue')
    except EOFError:
        break
