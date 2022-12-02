'''
파라메트릭 서치(매개변수 찾기)
단순 이진탐색이 아니라
이진 탐색으로 찾는 것이 문제를 푸는데 키포인트가 되는 요소 그 자체임
해당 요소를 찾아서 문제가 풀리는지 확인하는 것
공유기 설치는
주어지는 공유기를 모두 설치할 때
가장 인접한 공유기의 거리가 최대가 되는 것을 찾아야함
그렇다면, 이진 탐색으로 먼저 공유기 설치 거리를 정해놓고
그 거리를 통해 가장 인접한 공유기의 거리가 최대가 되는지 확인한다.
"이진 탐색을 통해 요소를 정하고, 되는지 확인 이런 느낌"
'''

N, C = map(int, input().split())

arr = []

for i in range(N) :
    arr.append(int(input()))
arr.sort()

start = 1
end = arr[-1]
result = 0
while start <= end :
    mid = (start+end)//2
    count = 1
    now = arr[0]
    for i in range(1, N):
        if arr[i] >= now+mid :
            now = arr[i]
            count += 1
    if count >= C :
        start = mid+1
        result = mid
    else :
        end = mid-1

print(result)
