def isvalid(s):
    stack = []
    for char in s:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if not stack:
                return False
            current_stack = stack.pop()
            if current_stack == '(':
                if char != ')':
                    return False
            if current_stack == '{':
                if char != '}':
                    return False
            if current_stack == '[':
                if char != ']':
                    return False
    if stack:
        return False
    return True


s = '(){}[]'
print(isvalid(s))
