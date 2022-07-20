def cal_takes(cut_point):
    s = 0
    for i in range(n):
        s += max(arr[i]-cut_point, 0)
    return s

n, m = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
end = max(arr)
mid = start

while True:
    takes = cal_takes(mid)
    if (takes == m) or (cal_takes(mid+1) < m and takes > m) :
        print(mid)
        break
    elif takes > m :
        start = mid
        mid = (end+mid)//2
    else :
        end = mid
        mid = (start+mid)//2