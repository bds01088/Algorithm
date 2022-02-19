'''
N개의 정수로 이루어진 수열이 있을 때
크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 
S가 되는 경우의 수를 구하는 프로그램을 작성

부분집합 만드는 bit연산자 사용해서 모두 만들고
그것들의 sum이 s랑 같은지 비교하기
'''

n, s = map(int, input().split())
l = list(map(int, input().split()))
cnt = 0
result = []
for i in range(1<<n):
    temp = []
    for j in range(n) :
        if i & (1<<j):
            temp.append(l[j])
    result.append(temp)

for p in result :
    if sum(p) == s and len(p) > 0:
        cnt += 1
print(cnt)

