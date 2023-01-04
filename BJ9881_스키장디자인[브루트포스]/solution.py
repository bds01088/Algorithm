N = int(input())

hills = []

for i in range(N):
    hills.append([int(input()), 0])

hills.sort()

mmax = hills[-1]
mmin = hills[0]

while True :
    minH = mmin[0]
    maxH = mmax[0]
    if maxH-minH <= 17 :
        break

    minCount = 0
    maxCount = 0
    for i in range(N):
        if hills[i][0] == minH :
            minCount += 1
        if hills[i][0] == maxH :
            maxCount += 1

    minCost = 0
    maxCost = 0
    #증가폭만 계산하는 것이 아니라 바꾸었을때 총 비용을 계산해서 비교해야한다
    #제곱의 값이기 때문에 그런듯
    for i in range(N):
        if i < minCount :
            minCost += (hills[i][1]+1)**2
            maxCost += (hills[i][1])**2
        elif i >= N-maxCount :
            minCost += (hills[i][1])**2
            maxCost += (hills[i][1]+1)**2
        else :
            minCost += (hills[i][1])**2
            maxCost += (hills[i][1])**2

    if minCost > maxCost :
        for i in range(N-1, N-maxCount-1, -1):
            hills[i][0] -= 1
            hills[i][1] += 1
        if hills[N-maxCount-1][0] >= hills[N-maxCount][0] :
            mmax = hills[N-maxCount-1]
        else :
            mmax = hills[N-maxCount]
        
    else :
        for i in range(minCount):
            hills[i][0] += 1
            hills[i][1] += 1
        if hills[minCount][0] <= hills[minCount-1][0] :
            mmin = hills[minCount]
        else :
            mmin = hills[minCount-1]

s = 0
for i in range(N):
    s += hills[i][1]**2
print(s)