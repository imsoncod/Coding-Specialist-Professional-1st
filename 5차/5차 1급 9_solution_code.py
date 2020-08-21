import queue

def solution(number, target):
	answer = 0
	visited = [0 for _ in range(10001)]
	q = queue.Queue()
	q.put(number)
	visited[number] = 1
	while not q.empty():
		x = q.get()
		if x == target:
			break
		if x+1 <= 10000 and visited[x+1] == 0:
			visited[x+1] = visited[x]+1
			q.put(x+1)
		if x-1 >= 0 and visited[x-1] == 0:
			visited[x-1] = visited[x]+1
			q.put(x-1)
		if 2*x <= 10000 and visited[2*x] == 0:
			visited[2*x] = visited[x]+1
			q.put(2*x)
	answer = visited[target]-1
	return answer