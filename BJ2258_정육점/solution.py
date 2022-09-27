import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

meats = []

for i in range(n):
    w, c = map(int, input().strip().split())
    meats.append([w, c])

meats.sort(key=lambda x: (x[1], -x[0]))
# print(meats)

s = 0
a = 0
flag = 0
for i in range(n):
    if i != 0 and meats[i-1][1] < meats[i][1] :
        a += s
        s = 0
    if meats[i][0]+a >= m :
        print(meats[i][1])
        flag = 1
        break
    s += meats[i][0]

if flag == 0 :

    print(-1)

'''
4 10
1 2
1 2
4 4
4 4

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
meats = []

for _ in range(N):
    meats.append(tuple(map(int,input().split())))

meats.sort(key=lambda x:(x[1],-x[0]))  # 가격 기준으로 싼 것부터 정렬 -> 가격 같으면 무게 큰 걸 먼저 정렬

dp = [0] * N # 해당 덩어리를 구매하면, 고기 양 얼마나 얻는지 

min_price = 2147483648
cnt = 1  # 가격 같은 것 여러 개 구매해야 할 때, 몇 개 구매해야 하는지 그 갯수

for i in range(len(meats)): # 가격 기준으로 쭉 돌아보기(싼 것부터)
    # 그 가격 이하의 고기 양 합이 필요한 양보다 많은지
    price = meats[i][1]

    if i != 0 and price == meats[i-1][1]:  # 가격 같은 것 여러 개 구매하는 경우
        cnt += 1
    else:
        cnt = 1

    dp[i] = dp[i-1] + meats[i][0]

    if dp[i] >= M:
        if price == meats[i-1][1]: # 가격 같은 것 여러 개 구매하는 경우
            min_price = min(price*cnt, min_price)

        else:  # 하나 구매하는 경우
            min_price = min(price, min_price)


if min_price == 2147483648: # 불가능한 경우
    print(-1)
else:
    print(min_price)
'''