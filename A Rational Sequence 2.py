# The label of the root is 1/1.
#
# The left child of label p/q is p/(p+q).
#
# The right child of label p/q is (p+q)/q.


for _ in range(int(input())):
    p, q = None, None
    _, label = map(int, input().split())
    l, r = label.spilit('/')
    if l < r:
        p = l
        q = r - p
    else:
        q = r
        p = r - q

    
