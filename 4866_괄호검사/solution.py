'''
여러 문자가 섞인 문자열이 들어오는데
그중 괄호들이 짝을 잘 이뤘는지 파악하자
(), {} 괄호가 있으며
{(})은 제대로 된 짝이 아니다
정상적이면 1 아니면 0을 출력
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
        if self.top == -1:
            return True
        else :
            return False


def isRight(n):
    stack = Stack(len(n))
    parenthesis = ["(", ")", "{", "}"]
    for x in n :
        if stack.top == -1 and x in parenthesis:
            if x != "(" and x != "{" :
                return 0
            else :
                stack.push(x)
        elif x in parenthesis :
            #여는 괄호 찾기
            if x == parenthesis[0] or x == parenthesis[2] :
                stack.push(x)
            #소괄호 닫기
            elif x == parenthesis[1] :
                if stack.arr[stack.top] != parenthesis[0] :
                    return 0
                else :
                    stack.pop()
            #중괄호 닫기
            elif x == parenthesis[3] :
                if stack.arr[stack.top] != parenthesis[2]:
                    return 0
                else:
                    stack.pop()
    if stack.isEmpty() :
        return 1
    else :
        return 0

tc = int(input())

for t in range(tc):
    s = input()
    result = isRight(s)
    print(f'#{t+1} {result}')