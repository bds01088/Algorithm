import sys
input = sys.stdin.readline

n = int(input().strip())

s = input().strip()

i = 0
num_list = []

while i < n :
    if s[i].isdigit() :
        snum = s[i]
        i += 1
        while i < n and s[i].isdigit():
            snum += s[i]
            i += 1
        num_list.append(int(snum))
    else :
        i += 1

print(sum(num_list))
