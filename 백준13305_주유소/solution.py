'''
이동하는데
현재 역 보다 싼 곳이 나타날때까지 갈 정도만 충전하거나,
마지막역 제외하고 남은 역들 중 값이 가장 작다면 끝까지 채우기
'''

n = int(input())

len_list = list(map(int, input().split()))
cost = list(map(int, input().split()))

s = 0
now = 0
mmin = min(cost[0:n-1])
while now < n :
    if cost[now] == mmin:
        s += cost[now]*sum(len_list[now:])
        break
    else :
        #now의 비용보다 더 싼 주유소를 찾을때까지 임시변수에 length값 누적더해주기
        next = now+1
        sl = cost[now]*len_list[now]
        while cost[now] < cost[next] :
            sl += len_list[next]*cost[now]
            next += 1
        s += sl
        now = next

print(s)