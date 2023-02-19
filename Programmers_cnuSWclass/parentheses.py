s = input()
stack = []
for i in s:
    if i == '(':
        stack.append('(')
    else:
        if not stack:
            stack.append(-1)
            break
        else:
            stack.pop()

if not stack:
    print('YES')
else:
    print('NO')
