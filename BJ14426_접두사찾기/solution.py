import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

word_list = []
for i in range(n) :
    word_list.append(input().strip())

cnt = 0

for i in range(m):
    s = input().strip()
    for word in word_list :
        if s == word[0:len(s)]:
            cnt += 1
            break
print(cnt)
    