book = [i for i in input().strip()]

left = list(book[0])
right = book[1:]
right.reverse()

for i in range(int(input())):
    act = input().strip()
    if act == 'move left' and len(left) > 1:
        right.append(left.pop())

    elif act == 'move right' and len(right) > 1:
        left.append(right.pop())

    elif act == 'tear left' and len(left) > 1:
        left.pop()

    elif act == 'tear right' and len(right) > 1:
        right.pop()

print(left[-1], right[-1], sep=' ')
