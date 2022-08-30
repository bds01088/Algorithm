import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().strip().split()))

arr.sort()

s = 0

for i in range(len(arr)):
    s += arr[i]*(len(arr)-i)

print(s)