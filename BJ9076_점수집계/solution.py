import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    arr = list(map(int, input().strip().split()))
    # print(arr)
    arr.sort()
    new_arr = arr[1:4]
    print(new_arr)
    if max(new_arr)-min(new_arr) >= 4 :
        print('KIN')
    else :
        print(sum(new_arr))