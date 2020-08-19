n = 4

def find_not_exist_nums(matrix):
    nums = []
    exist = []
    for i in range(n*n+1):
        exist.append(False)        
    for i in range(0, n):
        for j in range(0, n):
            if matrix[i][j] != 0:
                exist[matrix[i][j]] = True
    for i in range(1, n*n+1):
        if exist[i] == False:
            nums.append(i)
    return nums

def find_blank_coords(matrix):
    coords = []
    for i in range(0, n):
        for j in range(0, n):
            if matrix[i][j] == 0:
                coords.append([i, j])
    return coords

def is_magic_square(matrix):
    goal_sum = 0
    for i in range(1, n*n+1):
        goal_sum += i
    goal_sum //= n

    for i in range(0, n):
        row_sum = 0
        col_sum = 0
        for j in range(0, n):
            row_sum += matrix[i][j]
            col_sum += matrix[j][i]
        if row_sum != goal_sum:
            return False
        if col_sum != goal_sum:
            return False

    main_diagonal_sum = 0
    skew_diagonal_sum = 0
    for i in range(0, n):
        main_diagonal_sum += matrix[i][i]
        skew_diagonal_sum += matrix[i][n-1-i]

    if main_diagonal_sum != goal_sum:
        return False
    if skew_diagonal_sum != goal_sum:
        return False
    return True

def solution(matrix):
    answer = []
    coords = find_blank_coords(matrix)
    nums = find_not_exist_nums(matrix)

    matrix[coords[0][0]][coords[0][1]] = nums[0]
    matrix[coords[1][0]][coords[1][0]] = nums[1]
    if is_magic_square(matrix) == True:
        for i in range(0, 2):
            answer.append(coords[i][0] + 1)
            answer.append(coords[i][1] + 1)
            answer.append(nums[i])
    else:
        matrix[coords[0][0]][coords[0][1]] = nums[1]
        matrix[coords[1][0]][coords[1][1]] = nums[0]
        for i in range(0, 2):
            answer.append(coords[1-i][0] + 1)
            answer.append(coords[1-i][1] + 1)
            answer.append(nums[i])
    return answer