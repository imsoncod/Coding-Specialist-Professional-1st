vowels = ['A', 'E', 'I', 'O', 'U']
words = []

def create_words(lev, s):
    words.append(s)
    for i in range(0, 5):
        if lev < 5:
            create_words(lev + 1, s+vowels[i])

def solution(word):
    answer = 0
    create_words(0, '')
    words_n = len(words)
    for i in range(words_n):
        if word == words[i]:
            answer = i
            break
    return answer