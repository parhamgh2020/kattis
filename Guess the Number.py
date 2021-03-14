def binary_search(lst):
    m = len(lst) // 2
    print(lst[m])
    response = input()
    if response == 'lower':
        binary_search(lst[:m])
    elif response == 'higher':
        binary_search(lst[m:])
    else:
        return


binary_search(list(range(1, 1001)))
