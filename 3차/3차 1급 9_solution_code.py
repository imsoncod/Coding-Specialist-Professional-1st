def solution(revenue, k) :
    answer = 0
    n = len(revenue)
    rsum = sum(revenue[0:k])
    answer = rsum
    for i in range(k, n) :
        rsum = rsum - revenue[i-k] + revenue[i]
        if answer < rsum :
            answer = rsum
    return answer