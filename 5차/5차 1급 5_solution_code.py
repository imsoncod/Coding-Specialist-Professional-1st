def solution(enemies, armies):
	answer = 0
	enemies.sort()
	armies.sort()
	i, j = 0, 0
	while i < len(enemies) and j < len(armies):
		if enemies[i] <= armies[j]:
			answer = answer + 1
			i = i + 1
			j = j + 1
		else:
			j = j + 1
	return answer