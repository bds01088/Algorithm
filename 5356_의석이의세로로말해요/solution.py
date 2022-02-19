'''
A A B C D D
a f z z
0 9 1 2 1
a 8 E W g 6
P 5 h 3 k x
세로로 읽어서
위에껄 아래로 만들어야함
Aa0aPAf985Bz1EhCz2W3D1gkD6x
각 줄에는 길이가 1이상 15이하인 문자열이 주어진다.
각 문자열은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’만으로 이루어져 있다.
각 테스트 케이스는 총 다섯 줄로 이루어져 있다.

2중 for문을 써서 읽고
빈 문자열에 붙여넣기 하는데
불러올때 인덱스에러뜨면
try except로 스킵해주자
'''
import sys
sys.stdin = open("input.txt")

tc = int(input())
for t in range(tc):
    arr = []
    for _ in range(5):
        arr.append(list(input()))
    result = ''
    max_len = max(map(len, arr))
    for i in range(max_len):
        for j in range(5) :
            try:
                result += arr[j][i]
            except IndexError :
                continue
    print(f'#{t+1} {result}')
