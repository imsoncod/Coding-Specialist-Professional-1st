def solution(bishops):
    answer = 0

    alpha = ['A','B','C','D','E','F','G','H']
    chess = [[0] * 8 for _ in range(8)]
    dirx = [-1,-1,1,1]
    diry = [-1,1,1,-1]

    for pos in bishops:
        pos1 = int(pos[1]) - 1
        pos2 = alpha.index(pos[0])
        chess[pos1][pos2] = 1

        for i in range(4):
            q = [(pos1, pos2)]
            while q:
                x, y = q.pop(0)
                chess[x][y] = 1
                nx = x + dirx[i]
                ny = y + diry[i]
                if 0 <= nx < 8 and 0 <= ny < 8:
                    q.append((nx, ny))

    for i in chess:
        answer += sum(i)

    return 64 - answer