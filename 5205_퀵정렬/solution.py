'''
퀵 정렬을 구현해 n개의 정수를 정렬해 리스트a에 넣고
a[n//2]값을 출력하시오
'''

import sys
sys.stdin = open('input.txt')

def qsort(arr, start, end):
    #종료조건
    #재귀함수 계속돌다가 1개짜리가 되면
    #if문에서 start == end가 되므로 종료됌
    if start < end :
        new = partition(arr, start, end)
        #시작을 start부터 한다
        #0이 아니라
        qsort(arr, start, new-1)
        qsort(arr, new+1, end)

def partition(arr, start, end):
    pivot = arr[start]
    left = start
    right = end

    #교차되기 전까지~
    while left <= right :
        #피봇보다 작고(피봇보다 큰수를 찾을때 까지), right보다 작을 동안
        while left <= right and arr[left] <= pivot :
            left+=1
        #피봇보다 크고(피봇보다 작은 수를 찾을때 까지), left보다 클 동안
        while left <= right and arr[right] >= pivot :
            right-=1

        #위 while문이 두개 다 끝났을때
        #만약 교차되지 않은 상태로 끝났다면
        #(left는 피봇보다 큰수를 찾고, right는 피봇보다 작은수를 찾은 상황)
        #두개의 값을 변경함
        if left < right :
            arr[left], arr[right] = arr[right], arr[left]

    #교차되면 피봇이랑 위치 바꿔야됌
    arr[start], arr[right] = arr[right], arr[start]
    return right

tc = int(input())

for t in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    qsort(arr, 0, len(arr)-1)
    print(f'#{t+1} {arr[n//2]}')