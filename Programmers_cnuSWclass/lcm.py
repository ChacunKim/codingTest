def gcd(a, b):
    while(b):
        a, b = b, a%b
    return a

def lcm(a, b):
    # a*b = l * g, l = a*b/g
    return int((a * b)/gcd(a, b))

for test in range(int(input())):
    a, b = map(int, input().split())
    if a*b == lcm(a,b):
        print("Perfect")
    else:
        print("Not even close")