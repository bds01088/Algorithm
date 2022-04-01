'''
n종의 제품을 n곳의 공장에서 한 곳당 한가지씩 생산
생산비용이 주어질때 전체 제품의 최소 생산 비용을 구하시오

모두 탐색
visit는 공장만 하면 됨
제품은 DFS를 통해 모두 탐색 가능
제품0일때 DFS 안의 for문을 이용해 모든 공장들 탐색하면서
공장 중에 visit가 0인것만 방문하고
1로바꾼다음 다음 DFS로 들어가고
나오면 visit 0으로 바꾸기로

'''
import sys
sys.stdin = open('input.txt')

#DFS를 반복문 처럼 사용할 수 있다
#그러므로 product_num은 idx같은 것임
def DFS(product_num, cost):
    global ans, factory_visit
    #가지치기
    if cost > ans :
        return

    if product_num == n :
        if cost <= ans :
            ans = cost
        return
    else :
        for factory_num in range(n):
            if factory_visit[factory_num] == 0 :
                factory_visit[factory_num] = 1
                DFS(product_num+1, cost+board[product_num][factory_num])
                factory_visit[factory_num] = 0
        return ans

tc = int(input())

for t in range(tc):
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))
    ans = sum(map(sum, board))
    factory_visit = [0 for _ in range(n)]
    #제품 0번부터 싹 다 돌거니까 0을 넣자
    result = DFS(0, 0)
    print(f'#{t+1} {result}')
