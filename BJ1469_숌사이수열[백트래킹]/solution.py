'''
배열이 주어지고
해당 배열의 원소를 무조건 2개씩 포함하는 배열을 만들어야한다
만들어진 배열은 원소 i와 i 사이에 i개의 원소를 가지고 었는 배열이다
배열을 출력하되 여러개면 사전순으로 하나만 출력한다

하나씩 넣고 사용이 2가 되면 원소크기만큼 -idx한 값에 해당 원소가 존재하는지 확인하면 될듯
'''

import sys

input = sys.stdin.readline

def DFS(now, used):
    global answer
    if now != []:
        if len(now) == n*2 :
            tmp = now.copy()
            answer.append(tmp)
            return

    
    for i in range(n):
        if used[i] == 0 :
            used[i] += 1
            now.append(arr[i])
            DFS(now, used)
            now.pop()
            used[i] -= 1
        elif used[i] == 1 :
            if (len(now)-arr[i]-1 >= 0) and now[len(now)-arr[i]-1] == arr[i] :
                used[i] += 1
                now.append(arr[i])
                DFS(now, used)
                now.pop()
                used[i] -= 1
            else :
                continue
        else :
            continue


n = int(input().strip())

arr = list(map(int,input().strip().split()))

used = [0 for _ in range(n)]

answer = []

now = []

DFS(now, used)

if answer :
    for e in sorted(answer)[0] :
        print(e, end=' ')
else :
    print(-1)