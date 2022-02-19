'''
오름차순 정렬하자
'''
import sys
sys.stdin = open("input.txt")

tc = int(input())
for t in range(tc):
    n = int(input())
    l = list(map(int, input().split()))
    for i in range(len(l)-1, 0, -1) :
        for j in range(i):
            if l[j] > l[j+1] :
                l[j], l[j+1] = l[j+1], l[j]
    print(f'#{t+1}', end=' ')
    for x in l :
        print(x, end=' ')
    print()