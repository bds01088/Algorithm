'''
고를 수 있는 목록의 개수 n과 골라야하는 개수 m이 주어진다
중복해서 고르는게 가능하고
만들 수 있는 비내림차순의 수열을 모두 출력하라

4개의 수와 골라야할 2개
4 2
중복으로 고를 수 있어서 9가 여러개 들어오는건 상관없다
9 7 9 1

1 1
1 7
1 9
7 7
7 9
9 9
'''
def DFS(answer, idx):
    global arr
    if idx == m :
        for j in range(idx):
            print(answer[j], end=' ')
        print()
        return

    for i in range(len(arr)):
        if idx == 0 :
            answer[idx] = arr[i]
            DFS(answer, idx+1)
            answer[idx] = 0
        else :
            if answer[idx-1] <= arr[i] :
                answer[idx] = arr[i]
                DFS(answer, idx+1)
                answer[idx] = 0


n, m = map(int, input().split())

arr = list(map(int, input().split()))

#중복값 제거
arr = sorted(list(set(arr)))
answer = [0 for _ in range(m)]

DFS(answer, 0)