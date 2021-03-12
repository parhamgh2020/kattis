limit, event = list(map(int, input().split()))
capacity = 0
number_of_rejected_group = 0
for i in range(event):
    entrance, person = input().split()
    person = int(person)
    if entrance == "enter":
        if capacity + person <= limit:
            capacity += person
        else:
            number_of_rejected_group += 1
    elif entrance == "leave":
        capacity -= person

print(number_of_rejected_group)
