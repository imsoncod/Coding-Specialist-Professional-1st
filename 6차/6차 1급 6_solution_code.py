def solution(grid):
    answer = 0
    for i in range(4):
        for j in range(4):
            for k in range(j + 1, 4, 2):
                answer = max(answer, max(grid[i][j] + grid[i][k], grid[j][i] + grid[k][i]))
    return answer