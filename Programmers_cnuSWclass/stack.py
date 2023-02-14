'''
문제
push 와 pop 연산을 제공하는 스택을 구현해보자. 명세는 다음과 같다.

push x 스택에 정수 x (1 ≤ x ≤ 100 000)를 추가한다.
pop 스택에서 원소를 하나 제거하고 출력한다. 만약 스택이 비어있다면 -1 을 출력한다.
입력
첫째 줄에 연산의 개수 N (1 ≤ N ≤ 100 000) 이 주어진다.

둘째 줄 부터 N 개의 줄에 연산이 주어진다.

출력
N 개의 줄에 연산의 결과를 출력한다.
'''

stack = []
for i in range(int(input())):
    order = input()
    if order.startswith("push"):
        stack.append(int(order.replace("push ",'').strip()))
    else:
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)