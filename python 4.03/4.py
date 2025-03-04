def is_balanced(expression: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack


print(is_balanced('()()'))
print(is_balanced('({)})('))
print(is_balanced('ad()s(dsa)'))
print(is_balanced('(ad()s(dsa)'))
