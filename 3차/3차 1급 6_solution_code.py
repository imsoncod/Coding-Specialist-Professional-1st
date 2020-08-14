def solution(n):
    answer = 0
    prime = []
    prime.append(2)
    for i in range (3, n+1, 2) :
        for j in range(2, i) :
            if i % j == 0 :
                break
        if j == i - 1:
            prime.append(i)
        
    prime_n = len(prime)
    for i in range(0, prime_n - 2) :
        for j in range(i + 1, prime_n - 1) :
            for k in range(j + 1, prime_n) :
                if prime[i] + prime[j] + prime[k] == n :
                    answer += 1
    
    return answer