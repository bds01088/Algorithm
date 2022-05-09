'''
queue를 이용하여
중요도가 queue내에 가장 크다면
출력
아니면 가장 뒤로 보낸다
중요도가 같은 문서가 있으면 그냥 출력

몇번째에 출력되었는지 알고싶은 문서에다가
10을 더해주어서 유니크한 객체로 만들어주자
중요도는 1~9사이니까
중요도 비교할때는 %값으로 하면되고
'''
from collections import deque

tc = int(input())

for t in range(tc):
    n, m = map(int, input().split())
    q = deque()
    q.extend(list(map(int, input().split())))
    q[m] += 10
    cnt = 1
    while q :
        now = q.popleft()
        mmax = 0
        for i in range(len(q)):
            if q[i]%10 > mmax :
                mmax = q[i]%10
        if now%10 < mmax :
            q.append(now)
        else :
            if now > 10 :
                print(cnt)
                break
            cnt += 1



