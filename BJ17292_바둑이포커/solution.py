'''
16진수의 숫자와 색(b/w)가 주어진다
두장을 한쌍으로 포커를 진행하는데
1순위 연속된 수
2순위 같은 수
3순위 그 외

같은 서열 내에서도
1. 색이 같은 쌍
2. 큰 수가 큰쪽
3. 작은수가 큰 쪽
4. 큰수가 검은색

6장을 받으면 2장을 조합해 순서를 정렬하여 목록을 출력
'''
from itertools import combinations
# from pprint import pprint

def Ssort(arr):
    if len(arr) == 0 :
        return []
    cards = []
    for tcard in arr :
        continued = -1 if (tcard[0][0] + 1) % 15 == tcard[1][0] % 15 or (tcard[1][0] + 1) % 15 == tcard[0][0] % 15 else 1
        same = -1 if tcard[0][0] == tcard[1][0] else 1
        another = -1 if continued == 1 and same == 1 else 1
        s = str(hex(tcard[0][0])).replace('0x','') + tcard[0][1] + str(hex(tcard[1][0])).replace('0x','') + tcard[1][1]
        color = -1 if tcard[0][1]==tcard[1][1] else 1
        maxV = -max(tcard[0][0], tcard[1][0])
        minV = -min(tcard[0][0], tcard[1][0])
        mnumColor = tcard[0][1] if tcard[0][0] > tcard[1][0] else tcard[1][1]
        cards.append([continued, same, another, color, maxV, minV, mnumColor, s])
    cards.sort(key=lambda x : (x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))
    return cards

arr = list(list(map(lambda x : [x[0],x[1]], input().split(','))))

for i in range(6):
    arr[i][0] = int(arr[i][0],16)

# pprint(list(combinations(arr, 2)))
new_arr = list(combinations(arr, 2))


for ele in Ssort(new_arr):
    print(ele[-1])

"""
이상하게 대분류 3가지로 먼저 분리한다음
소분류로 넘겨주고 그 결과값을 합치면 틀림

contin_arr = []
same_arr = []
rest_arr = []

for i in range(len(new_arr)) :
    if abs(new_arr[i][0][0]%15-new_arr[i][1][0]%15) == 1 :
        contin_arr.append(new_arr[i])

    elif new_arr[i][0][0] == new_arr[i][1][0] :
        same_arr.append(new_arr[i])

    else :
        rest_arr.append(new_arr[i])

result = Ssort(contin_arr)+Ssort(same_arr)+Ssort(rest_arr)
# pprint(result)
for i in range(len(result)):
    print(result[i][-1])

# pprint(Ssort(contin_arr))
# pprint(Ssort(same_arr))
# pprint(Ssort(rest_arr))"""