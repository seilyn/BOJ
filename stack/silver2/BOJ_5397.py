case = int(input())

for _ in range(case):

    string = str(input())
    left = []
    right = []

    cursor = 0

    for char in string:
        if char == '<':
            if left:
                right.append(left.pop())
        elif char == '>':
            if right:
                left.append(right.pop())

        elif char == '-':
            if left:
                left.pop()

        else:
            left.append(char)

    left.extend(reversed(right))

    print(''.join(left))