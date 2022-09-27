'''
1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

결론
하나의 색을 i번째에서 선택을 했다면,
그 이전(i-1)번째에서 i번째 선택한 색을 제외한 것들 중 가장 적은 비용을 구해서
i번째 색을 선택한 최소비용이 계산된다.
'''

import sys

input = sys.stdin.readline

n = int(input().strip())

RGB = []
for _ in range(n):
    RGB.append(list(map(int, input().strip().split())))

# print(RGB)
for i in range(1, n):
    # print(RGB[i])
    RGB[i][0] += min(RGB[i-1][1],RGB[i-1][2])
    RGB[i][1] += min(RGB[i - 1][0], RGB[i - 1][2])
    RGB[i][2] += min(RGB[i - 1][0], RGB[i - 1][1])

print(min(RGB[n-1]))