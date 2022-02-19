'''
str1, str2가 주어짐
2안에 1과 일치하는 부분이 있으면
출력1
없으면 0출력

'''

import sys
sys.stdin = open("input.txt")

tc = int(input())

#brute force
def isin(str1, str2):
    for i, c in enumerate(str2) :
        if c == str1[0] :
            if str2[i:i+len(str1)] == str1 :
                return 1
    return 0

for t in range(tc):
    str1 = input()
    str2 = input()
    result = isin(str1, str2)
    print(f'#{t+1} {result}')