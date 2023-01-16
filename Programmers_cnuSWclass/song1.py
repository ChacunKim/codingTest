n = int(input())
titles = [input() for t in range(n)]

sec = []
for s in range(n):
    song_sec = int(input())
    if s == 0:
        sec.append(song_sec)
    else:
        sec.append(sec[s-1] + song_sec)
print(titles)
print(sec)
idx = 0
for q in range(int(input())):
    q_sec = int(input())
    print(q_sec)
    for i, s in enumerate(sec[idx:]):
        if q_sec <= s:
            print(titles[i])
            break




