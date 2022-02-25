'''
8개의 숫자를 입력받고
입력 받은 위치의 인덱스+1 값을 숫자에서 빼고
맨뒤로 이동시킨다
이를 5번 반복하고 이것을 한 사이클이라 한다
사이클을 반복하던 중 0보다 작아지거나 0일 경우 0으로 저장되며 반복을 끝낸다

해결방법
큐를 쓰되
0~4까지 인덱스+1값을 해당 값에서 빼주고 맨뒤로 이동시키고
한 사이클이 끝나면
이를 다시 기준으로 잡고 반복
'''

import sys
sys.stdin = open("input.txt")
'''
class Queue:

    # createQueue
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        # 원형큐의 경우, 고의적으로 큐의 공백을 하나 만들어 두고 사용한다.
        self.rear = 0
        self.front = 0

    def enQueue(self, el):
        if self.isFull():
            # 여러가지 해결방법
            # 1. queue의 크기를 늘린다.
            # 2. 또다른 예외처리
            print('Queue is Full!!')
        else:
            # rear의 값을 조정하는 방법
            '''
            #(rear + 1) % self.size
            '''
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = el

    def deQueue(self):
        if self.isEmpty():
            print('Queue is Empty!!')
        else:
            self.front = (self.front + 1) % self.size
            return self.items[self.front]

    def isEmpty(self):
        # 선형 큐에서 큐가 비어 있다는 뜻
        return self.rear == self.front

    def isFull(self):
        # rear가 front의 바로 뒤에 위치 할때
        return self.front == (self.rear + 1) % self.size

    def QPeek(self):
        return self.items[self.front]
'''

for _ in range(10):
    t = int(input())
    password = list(map(int, input().split()))
    #마지막 값이 0일때까지
    while password[-1] != 0 :
        #1부터 5까지 반복 (1사이클)
        for i in range(1,6):
            #첫값 추출
            target = password.pop(0)
            #추출값에서 i값빼주고
            target -= i
            #그 값이 0보다 작거나 같으면
            if target <= 0 :
                #0으로 바꾸고
                target = 0
                #추가하고
                password.append(target)
                #더이상 반복문 수행할 이유가 없음
                break
            else :
                password.append(target)
    print(f'#{t}', end=' ')
    #리스트를 숫자별로 출력할때 언팩쓰면 편하다
    print(*password)
    # for i in range(8):
    #     print(password[i], end=' ')
    # print()



