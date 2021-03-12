set_counter = 1
while True:
    input_1 = int(input())
    if input_1 == 0:
        break
    else:
        l = list()
        for _ in range(input_1):
            l.append(input())
        l.sort(key=len)
        # list_demanded = list()
        # for i in range(len(l)):
        # if i % 2 == 0:
        #     list_demanded.insert(0, l[i])
        # else:
        #     list_demanded.append(l[i])
        list_demanded = l[::2] + l[1::2][::-1]
        print('SET {}'.format(set_counter))
        set_counter += 1
        for i in list_demanded:
            print(i)

# setno = 1
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     else:
#         current_set = []
#         for i in range(a):
#             name = input()
#             current_set.append(name)
#         ans_set = current_set[::2]+current_set[1::2][::-1]
#         print("SET {}".format(setno))
#         for j in ans_set:
#             print(j)
#         setno+=1
#
#
#
