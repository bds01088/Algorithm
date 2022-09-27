''' 
!!!!!!!!!!!!!!!!!!!재준님 풀이!!!!!!!!!!!!!!!!!!!
def solution(today, terms, privacies):
    def date_to_day(date):
        y, m, d = map(int, date.split('.'))
        res = y * 12 * 28 + m * 28 + d
        return res

    answer = []
    d = dict()
    for term in terms:
        ytype, due = term.split()
        d[ytype] = int(due)

    today = date_to_day(today)
    for i in range(len(privacies)):
        date, ytype = privacies[i].split()
        expire_date = date_to_day(date) + d[ytype] * 28

        if expire_date <= today:
            answer.append(i+1)

    return answer
'''
def solution(today, terms, privacies):
    answer = []

    dateList = []

    dateList.append(list(map(int, today.split("."))))

    termDic = {}
    
    for t in terms :
        tType, month = t.split()
        month = int(month)
        termDic[tType] = month

    for p in privacies:
        pDate, pType = p.split()
        pDate = list(map(int, pDate.split(".")))
        pDate[1] += termDic[pType]
        if pDate[1] > 12 :
            pDate[0] += pDate[1]//12
            pDate[1] = (pDate[1]-1)%12+1
        pDate[2] -= 1
        if pDate[2] == 0 :
            pDate[2] = 28
            pDate[1] -= 1
            if pDate[1] == 0 :
                pDate[1] = 12
                pDate[0] -= 1
        
        dateList.append(pDate)
    
    print(dateList)
    for i in range(1, len(dateList)):
        if dateList[0][0] > dateList[i][0] :
            answer.append(i)
            continue
        if dateList[0][1] > dateList[i][1] :
            answer.append(i)
            continue
        if dateList[0][2] > dateList[i][2] :
            answer.append(i)
            
    return answer


_t = "2020.01.01"
_a = ["Z 3", "D 5"]
_p = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
print(solution(_t, _a, _p))