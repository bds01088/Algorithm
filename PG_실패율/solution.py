def solution(N, stages):
    answer = []
    
    rate_arr = [[i, 0] for i in range(0, N+2)]
    
    stages.sort()
    
    total = len(stages)

    cnt = 0
    for i in range(len(stages)) :
        rate_arr[stages[i]][1] += 1

        if i != 0 and stages[i] != stages[i-1] :
            rate_arr[stages[i-1]][1] /= total
            total -= cnt
            cnt = 0
        if i == len(stages)-1 :
            rate_arr[stages[i]][1] /= total
            
        cnt += 1
            
    answer = sorted(rate_arr, key=lambda x : x[1], reverse=True)
    print(answer)    
    ans = []
    
    for i in range(len(answer)):
        if 1 <= answer[i][0] <= N :
            ans.append(answer[i][0])
    
    return ans

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

print(solution(4,[4,4,4,4,4]))