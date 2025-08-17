import keyboard
painting_order = open('paintingorder.txt', 'r').read()
painting_order = painting_order.strip().split('|')
print(painting_order)
for x in range(len(painting_order)):
    painting_order[x] = painting_order[x].strip().split()
print(painting_order)

# List that keeps track of the selected letter for each position
selected = []
for x in painting_order:
    selected.append(0)

# The letter the user is currently modifiying
selector = 0

while True:
    print_string = ""
    max_length = 0
    for x in painting_order:
        max_length = max(max_length, len(x))
    for x in painting_order:
        if len(x) < max_length:
            for i in range(max_length - len(x)):
                x.append(' ')
    for i in range(max_length):
        for x in painting_order:
            print_string += x[i - int(max_length/2)] + ' '
        print_string += '\n'
        if i == max_length - 1:
            for y in range(selector):
                print_string += '  '
            print_string += '^'
    print(print_string)

    while True:
        if keyboard.is_pressed('right'):
            selector += 1
            if selector >= len(painting_order):
                selector = 0
            break
        if keyboard.is_pressed('left'):
            selector -= 1
            if selector < 0:
                selector = len(painting_order) - 1
            break
        if keyboard.is_pressed('up'):
            selected[selector] += 1
            if selected[selector] >= len(painting_order[selector]):
                selected[selector] = 0
            break
        if keyboard.is_pressed('down'):
            selected[selector] -= 1
            if selected[selector] < 0:
                selected[selector] = len(painting_order[selector]) - 1
            break
    print("\033c", end="")