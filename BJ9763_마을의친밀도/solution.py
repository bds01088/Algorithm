import sys

input = sys.stdin.readline

n = int(input().strip())

town_list = []

for i in range(n):
    x, y, z = map(int, input().strip().split())
    town_list.append((x, y, z))


ans = 999999

for town in town_list:
    minDist1 = 99999
    minDist2 = 99998
    for anotherTown in town_list :
        if town != anotherTown :
            dist = abs(town[0]-anotherTown[0]) + abs(town[1]-anotherTown[1]) + abs(town[2]-anotherTown[2])
            if dist < minDist1 or dist < minDist2 :
                if minDist1 <= minDist2 :
                    minDist2 = dist
                else :
                    minDist1 = dist
    score = minDist1 + minDist2
    if ans > score:
        ans = score
        
print(ans)

'''
동욱님 코드인데, tuple로 받는거랑, 비교로직이랑 두개 다 이렇게 해야 겨우 통과하는 억까문제
import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    x, y, z = map(int, input().split())
    arr.append((x, y, z))

# ? -- center -- ? / min 1, min 2
ans = 10010
for center in range(n):
    min_1 = 5000
    min_2 = 5010
    for j in range(n):
        if not j == center:  # 자기자신은 할 필요 없다
            dist = abs(arr[center][0] - arr[j][0]) \
                   + abs(arr[center][1] - arr[j][1]) + abs(arr[center][2] - arr[j][2])
            if dist >= min_2:
                continue
            elif dist <= min_1:
                # min_1 <-dist, min_2 <-min_1
                min_1, min_2 = min_2, min_1
                min_1 = dist
            else:  # min_1 < dist < min_2
                min_2 = dist
    temp = min_1 + min_2
    if temp < ans:
        ans = temp

print(ans)
'''