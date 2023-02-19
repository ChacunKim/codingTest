string = sorted(list(set(input().replace(' ','').upper())))
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print('YES') if len(string) == len(alphabet) else print('NO')