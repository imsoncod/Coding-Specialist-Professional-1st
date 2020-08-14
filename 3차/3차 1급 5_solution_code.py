def solution(phrases, second):
	answer = ''

	display = '______________' + phrases
	for i in range(second):
		display = display[1:] + display[0]
	answer = display[:14]
	return answer
