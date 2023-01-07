a, b = map(int, input().strip().split())

def findGcd(a, b):
    r = a%b
    if r == 0:
        return b
    else:
        return findGcd(b, r)

print(findGcd(a, b))