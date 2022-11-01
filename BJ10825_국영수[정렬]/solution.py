import sys

input = sys.stdin.readline

n = int(input().strip())

arr = []

for i in range(n):
    name, K, E, M = input().strip().split()
    arr.append((name, int(K), int(E), int(M)))


sort_arr = sorted(arr, key=lambda x : (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(sort_arr[i][0])