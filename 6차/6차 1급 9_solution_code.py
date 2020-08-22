def func_a(stack):
    return stack.pop()

def func_b(stack1, stack2):
    while not func_c(stack1):
        item = func_a(stack1)
        stack2.append(item)

def func_c(stack):
    return (len(stack) == 0)

def solution(stack1, stack2):
    if func_c(stack2):
        func_b(stack1, stack2)

    answer = func_a(stack2)
    return answer

ret1 = solution([1,2], [3,4])
ret2 = solution([1,2,3], [])
