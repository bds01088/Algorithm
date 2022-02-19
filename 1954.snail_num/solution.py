'''
1부터 n*n까지의 숫자가 시계방향으로 이루어지도록 출력하자

ex)
3
1 2 3
8 9 4
7 6 5
'''

#델타하고싶었는데 못했고..
#그냥 때려박는것도 못해서
#검색해버렸네..
import sys
sys.stdin = open("input.txt")

def snail(n) :
    s = []
    for i in range(n) :
        q = []
        for j in range(n) :
            q.append(0)
        s.append(q)
    num = 1
    row = 0
    col = -1 #맨처음에는 0으로 시작하게 되면 방향전환이 이루어진 뒤에 이미 수가 있는 위치에 입력되기때문에 증가시켜주고 시작해야되서 -1넣음
    d = 1 #방향설정은 늘었다 줄었다를 하기 위해 -1을 곱하려고 변수로 따로 지정해줘야함
    while n > 0 :
        for _ in range(n) : #col 증가용 for문
            col += d #증가하고 시작
            s[row][col] = num
            num += 1
        n -= 1 #달팽이 배열 특성상 방향전환하면 그뒤에 넣어야되는 길이가 1씩 줄어든다
        for _ in range(n) :
            row += d
            s[row][col] = num
            num += 1
        d *= -1 #방향이 col증가 row증가 col감소 row감소 순서이므로 col, row for문을 두개 돌고 방향전환한다
    return s

tc = int(input())

for t in range(tc) :
    n = int(input())
    print(f'#{tc+1}')
    print(snail(n))


#델타로 푼 방식
'''
# row, col 인덱스로 탐색할 수 있게 방향 설정 (달팽이 방향이니까 우->하->좌->상)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    # 초기 위치 & 회전방향 설정
    r, c = 0, 0
    dist = 0  # 0:우, 1:하, 2:좌, 3:상

    for n in range(1, N*N + 1):
        snail[r][c] = n
        r += dr[dist]
        c += dc[dist]

        # 범위를 벗어나거나 0이 아닌 다른 값이 이미 있다면, dist 방향 체인지
        # 근데 이런 경우라면 요소 인덱스를 다시 원위치시켜줘야하므로 빼줘야함
        # 그런다음 dist의 방향을 바꾸고, 방향 바꿨으면 다시 움직일 수 있도록 행렬 인덱스 업데이트
        if r < 0 or c < 0 or r >= N or c >= N or snail[r][c] != 0:
            # 실행취소
            r -= dr[dist]
            c -= dc[dist]
            # dist는 % 4 안해주면 0123, 4567, ... 이런식으로 숫자 커지므로 나머지로 접근
            dist = (dist + 1) % 4
            #  다시 gogo
            r += dr[dist]
            c += dc[dist]

    print("#{}".format(tc))
    for row in snail:
        print(*row)
    print()
'''