case = int(input())

for _ in range(case):

    string = str(input())
    temp = []

    cursor = 0

    for char in string:
        if char == '<':
            if cursor != 0:
                cursor -= 1
                if cursor < 0:
                    cursor = 0

        elif char == '>':
            cursor += 1
            if cursor > len(temp):
                cursor = len(temp)

        elif char == '-':
            if temp:
                if cursor <= 0:
                    cursor = 0
                else:
                    temp.pop(cursor-1)
                    cursor -= 1
        else:
            # temp.append(char)
            temp.insert(cursor, char)
            cursor += 1



    print(''.join(temp))
