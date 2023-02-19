n = int(input())
lengths = list(map(int, input().split()))

prefix = [1]
tmp = 0
for i in range(n):
    tmp += lengths[i]
    prefix.append(tmp)
print(prefix)
m = int(input())
questions = list(map(int, input().split()))

answer = []
total = 0
songNum = 1
for i in range(m):
    q = questions[i]
    if q > prefix[-1]:
        last = prefix[-1]
        prefix = [x + last for x in prefix]
        print(prefix)
        songNum = 1

    if q > prefix[songNum]:
        songNum += 1

    total = (total + songNum) % 1000000007
    answer.append(songNum)
print(answer)
print(total)

