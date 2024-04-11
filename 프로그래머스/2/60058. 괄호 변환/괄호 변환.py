
def solution(p):
    # ()의 개수가 같다면 균형잡힌 문자열
    # ()의 괄호의 짝도 모두 맞을 경우에는 올바른 괄호 문자열
    if p == '': #1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
        return ''
    u, v = divide_w(p)

    if correct_str(u):
        u = u + solution(v)
        return u
    else:
        temp = '(' + solution(v) + ')'
        # u의 첫 번째와 마지막 문자를 제거
        u = u[1:-1]

        for i in range(0, len(u)):
            if u[i] == '(':
                temp = temp + ')'
            else:
                temp = temp + '('
        return temp

def correct_str(w):
    stack = []
    for i in range(len(w)):
        if w[i] == '(':
            stack.append(w[i])
        else: # w[i]==')'
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    if len(stack) > 0:
        return False

    return True

def divide_w(w):
    left = 0
    right = 0
    u = ''
    v = ''
    for i in range(len(w)):
        if w[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break

    u = w[:(left + right)]
    v = w[(left + right):]
    print("u=",u,"v=",v)
    return u, v
