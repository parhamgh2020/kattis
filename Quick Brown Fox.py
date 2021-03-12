for _ in range(int(input())):
    letters = [chr(i) for i in range(97, 97 + 26)]
    input_ = set(input().lower())
    for i in input_:
        if i in letters:
            letters.remove(i)
    print(f'missing {format("".join(letters))}' if letters else 'pangram')
