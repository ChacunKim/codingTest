q = []
for i in range(int(input())):
    order = input()
    if order.startswith("push"):
        q.append(int(order.replace("push ","")))
    else:
        if len(q) > 0:
            print(q.pop(0))
        else:
            print(-1)