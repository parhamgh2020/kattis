# import sys
#
# d = set()
# for line in sys.stdin:
#     out_line = []
#     for word in line.split():
#         if word.upper() in d:
#             out_line += ['.']
#         else:
#             d.add(word.upper())
#             out_line += [word]
#             # print(out_line)
#     print(" ".join(out_line))

import sys

inp = set()
for line in sys.stdin:
    out = []
    for word in line.split():
        if word.upper() not in inp:
            out.append(word)
        else:
            out.append('.')
        inp.add(word.upper())
        # print(inp)

    print(" ".join(out))
