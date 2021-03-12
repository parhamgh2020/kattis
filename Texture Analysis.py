def model(string):
    dot = 0
    star = 0
    if string == '*':
        return dot, 1
    for i in range(1, len(string)):
        if string[i] == '.':
            dot += 1
        if string[i] == '*':
            star += 1
        if string[i] == '*' and dot > 0:
            return dot, star
    return dot, star


def find_even(string, model):
    dot, star = model(string)
    len_model = model[0] + model[1]
    for i in range(0, len(string),len_model):

