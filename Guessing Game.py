start = 0
end = 11
while True:
    number = int(input())
    if number == 0:
        break
    response = input()
    if response == 'too low' and number > start:
        start = number
    elif response == 'too high' and number < end:
        end = number
    if response == 'right on':
        if start < number < end:
            print('Stan may be honest')
        else:
            print('Stan is dishonest')
        start, end = 0, 11
