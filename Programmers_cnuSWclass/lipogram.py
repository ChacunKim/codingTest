string = sorted(set(input().replace(' ','').lower()))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
if len(string) != len(alphabet):
    for s in string:
        alphabet = alphabet.replace(s, '')
    print('YES\n'+alphabet)
else:
    print('NO')