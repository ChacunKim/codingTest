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
        songNum = 1
        q -= prefix[-1]

    if q > prefix[songNum]:
        songNum += 1

    total = (total + songNum) % 1000000007
    answer.append(songNum)
print(answer)
print(total)

