import sys

input = lambda : sys.stdin.readline().strip()

N, M = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
start = arr[-1]-M
end = arr[-1]
ans = 0

while start <= end :
    mid = (start+end)//2
    s = 0
    for i in range(len(arr)):
        # if arr[i]-mid <= 0 :
        #     s += 0
        # else :
        #     s += arr[i]-mid
        s += max(arr[i]-mid, 0)
    if s < M :
        end = mid-1
    else :
        ans = mid
        start = mid+1
    
print(ans)
