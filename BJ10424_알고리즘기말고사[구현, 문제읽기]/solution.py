import sys

input = lambda : sys.stdin.readline().strip()
n = int(input())

arr = list(map(int, input().split()))
ans = [0 for _ in range(n)]
#기말고사 성적 순으로 중간고사 성적이 들어옴
#출력은 중간고사 등수를 기준으로 기말고사 성적 만족도 출력
#입력 출력 문제를 잘 읽자
for i in range(n):
    mid = arr[i]
    last = i+1
    ans[mid-1] = mid-last

for i in range(n):
    print(ans[i])