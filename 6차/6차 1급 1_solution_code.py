import queue

def solution(n, garden):
    answer = 0

    q = queue.Queue()
    dx = [ -1, 1, 0, 0 ]
    dy = [ 0, 0, -1, 1 ]

    for i in range(n) :
    	for j in range(n) :
    		if garden[i][j] == 1 :
    			q.put((i, j, 0))

    while q.empty() == False :
    	x, y, day = q.get()

    	for i in range(4) :
    		next_x = x + dx[i]
    		next_y = y + dy[i]
    		next_day = day + 1

    		if (0 <= next_x and next_x < n and 0 <= next_y and next_y < n) and (garden[next_x][next_y] == 0) :
    			garden[next_x][next_y] = 1
    			answer = next_day
    			q.put((next_x, next_y, next_day))

    return answer