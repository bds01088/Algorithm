import sys
input = sys.stdin.readline

'''
누적합 문제
일단 누적된 합들을 구하고
일정 범위의 합을 구하는건
해당 범위까지 합에서 일정 범위의 시작 위치의 합을 빼는 것이다.
'''

n, m = map(int, input().strip().split())

arr = list(map(int, input().strip().split()))

s = 0
sarr = []
for i in range(len(arr)):
    s += arr[i]
    sarr.append(s)

for _ in range(m):
    start, end = map(int, input().strip().split())
    if start-1 == 0 :
        result = sarr[end-1]
    else :
        result = sarr[end-1]-sarr[start-2]
    print(result)