import sys

input = lambda : sys.stdin.readline().strip()

n = int(input())

have_arr = list(map(int, input().split()))

have_arr.sort()

m = int(input())

req_arr = list(map(int, input().split()))

for target in req_arr :
    start = 0

    end = len(have_arr)

    flag = 0
    while start <= end :
        mid = (start+end)//2

        if have_arr[mid] == target :
            print("yes", end=' ')
            flag = 1
            break
        elif have_arr[mid] > target :
            end = mid-1
        else :
            start = mid+1
    if not flag :
        print("no", end=' ')
    
