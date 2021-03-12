class Tree:
    def __init__(self, val=None):
        self.val = val
        self.right = None
        self.left = None

    def add(self, val):
        if self.val is None:
            self.val = val
        elif val > self.val:
            if self.right is None:
                self.right = Tree(val)
            else:
                self.right.add(val)
        else:
            if self.left is None:
                self.left = Tree(val)
            else:
                self.left.add(val)


n_test, layers = map(int, input().split())
shapes = set()
for i in range(n_test):
    tr = Tree()
    for val in list(map(int,input().split())):
        tr.add(val)
    q = [tr]
    string = str()
    while len(q):
        node = q.pop()
        string += 'l' if node.left else 'n'
        string += 'r' if node.right else 'n'
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    shapes.add(string)
print(len(shapes))

