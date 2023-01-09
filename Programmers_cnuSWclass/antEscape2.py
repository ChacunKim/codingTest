testCase = int(input())

for i in range(testCase):
    len, crush = map(int, input().strip().split())
    world = input()
    ant = world.find('@')
    exitW = world.find('O')
    if ant>exitW:
        world = world[exitW:ant]

    else:
        world = world[ant: exitW]

    wall = world.count('#')
    if wall > crush:
        print('HELP!')
    else:
        print('HAHA!')

