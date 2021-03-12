import fileinput

variable = {}
compare = {
    '=': lambda a, b: variable[a] == variable[b],
    '>': lambda a, b: variable[a] > variable[b],
    '<': lambda a, b: variable[a] < variable[b]
}
bool_tx = {True: 'true', False: 'false'}

for line in fileinput.input():
    inp = line.split()
    if inp[0] == 'define':
        variable[inp[2]] = int(inp[1])
    else:
        if inp[1] not in variable or inp[3] not in variable:
            print('undefined')
        else:
            print(bool_tx[compare[inp[2]](inp[1], inp[3])])
