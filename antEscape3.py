'''
문제 설명
개미 탈출 3
문제
준식이는 길이가 N 인 1차원 세상의 어딘가에 위치해 있고, 1차원 세상의 어딘가에 위치한 탈출구로 이동하려고 한다. 준식이는 1차원 세상에서 현재 위치한 칸에서 왼쪽 칸이나 오른쪽 칸으로 움직일 수 있다. 준식이가 가는 길에 벽이 있을 수도 있다. 준식이는 화가 많이 났기 때문에 주먹으로 최대 M 개의 벽을 부수고 지나갈 수 있다.

그런데 어느 날, 1차원 세상에 인피니티 건틀렛이 떨어졌다. 준식이가 인피니티 건틀렛이 있는 칸으로 이동해서 손에 끼고 손가락을 튕기기만 하면 1차원 세상의 모든 벽을 부술 수 있다.

7 1
#O###@G
준식이가 위치한 1차원 세상을 표현한 지도가 주어질 때 준식이는 1차원 세상을 탈출할 수 있을지 구해보자.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스의 첫째 줄에 1차원 세상의 길이 N (3 ≤ N ≤ 8) 와 준식이가 벽을 부술 수 있는 최대 횟수 M (0 ≤ M ≤ N - 3)

둘째 줄에 1차원 세상을 표현한 길이 N 짜리 문자열 S 가 주어진다.

문자열에서 @ 는 단 한 번 등장하며, 준식이를 의미한다.

문자열에서 알파벳 대문자 O 는 단 한 번 등장하며, 준식이가 이동하려는 탈출구를 의미한다.

문자열에서 알파벳 대문자 G 는 단 한 번 등장하며, 인피니티 건틀렛을 의미한다.

나머지 위치의 문자는 . 이거나 # 이다. . 은 빈 칸을 의미한다. 준식이는 빈 칸으로 자유롭게 이동할 수 있다. # 은 벽을 의미한다. 준식이는 벽이 있는 칸으로 이동할 수 없지만, 최대 M 개의 벽은 부술 수 있다.

출력
각 테스트 케이스마다 준식이가 1차원 세상을 탈출할 수 있다면 HAHA! 를 출력한다. 그렇지 못하다면 HELP! 를 출력한다. 모두 대문자로 출력해야 하는 것에 유의한다.

예제 입력 1
4
7 1
@####OG
8 2
G###@##O
8 2
O###@##G
5 0
OG##@
예제 출력 1
HELP!
HAHA!
HAHA!
HELP!
'''

'''
주가 테스트 케이스
6
7 3
#@###OG
15 3
...G#..###@###O
15 3
..G#..###@####O
15 2
...G#..###@###O
8 0
.#..##@O
10 1
.#..##@#O

결과
HAHA!
HAHA!
HELP!
HELP!
HAHA!
HAHA!
'''
testCase = int(input())

for i in range(testCase):
    length, crush = map(int, input().strip().split())
    world = input().replace('.','')

    ant = world.find('@')
    start = ant-crush-1

    world2 = world
    if start > 0:
        world2 = world[start:]
        ant = world2.find('@')
        print(f'ant: {ant} | crush: {crush} | start: {start} | len: {len(world2)}')
        print(world2)

    end = ant+crush+2
    if end < len(world2):
        world2 = world2[:end]
        print(f'ant: {ant} | crush: {crush} | end: {end} | len: {len(world2)}')

    print(world2)

    if 'G' in world2 or 'O' in world2:
        print('HAHA!')
    else:
        print('HELP!')










