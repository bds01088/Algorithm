def cal_takes(cut_point):
    s = 0
    for i in range(n):
        s += max(arr[i]-cut_point, 0)
    return s

n, m = map(int, input().split())

arr = list(map(int, input().split()))

start = max(arr) - m
end = max(arr)
num = start

while True:
    aaa = cal_takes(num)
    if (aaa == m) or (cal_takes(num+1) < m and cal_takes(num) > m) :
        print(num)
        break
    elif aaa > m :
        num = (end+num)//2
    else :
        num = (start+num)//2