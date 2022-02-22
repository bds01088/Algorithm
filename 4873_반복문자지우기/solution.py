'''
문자열에서 반복된 문자를 지우려 한다
지워진 부분은 다시 앞뒤를 연결하며
연결에 의해 반복문자가 된다면 다시 지운다

CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.
CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.
CAA 연속 문자 AA를 지운다.
C 1글자가 남았으므로 1을 리턴한다.
'''

import sys
sys.stdin = open("input.txt")

class Stack :
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.arr = [None]*size

    def push(self, n):
        self.top += 1
        self.arr[self.top] = n

    def pop(self):
        self.top -= 1
        return self.arr[self.top+1]

    def isEmpty(self):
        if self.top == -1 :
            return True
        else :
            return False

    def isFull(self):
        if self.top == self.size-1 :
            return True
        else :
            return False


def del_dup(s):
    stack = Stack(len(s))
    for x in s :
        if stack.top == -1 :
            stack.push(x)
        else :
            #stack[stack.top]은 불가능
            #stack[stack.top]쓰면 stack object is not subscriptable 에러 뜸
            #stack은 Stack의 인스턴스임, 즉 스택 그자체
            #스택을 리스트처럼 뽑아내려면 stack.arr을 써줘야한다
            if stack.arr[stack.top] == x :
                stack.pop()
            else :
                stack.push(x)
    return stack.top+1

tc = int(input())

for t in range(tc):
    s = input()
    result = del_dup(s)
    print(f'#{t+1} {result}')
