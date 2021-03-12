from statistics import mean as avr
import fileinput
for line in fileinput.input():
    h_bits = []
    name = str()
    for i in line.split():
        if i[0].isdigit():
            h_bits.append(float(i))
        else:
            name += ' ' + i
    print(avr(h_bits), name)
