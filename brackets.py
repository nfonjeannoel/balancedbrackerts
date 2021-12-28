def areBracketsSame(expr):
    stack = []
    for char in expr:
        if char in ["[", "{", "("]:
            stack.append(char)
        else:
            if not stack:
                return False
            cur = stack.pop()
            if cur == "[":
                if char != "]":
                    return False
            if cur == "{":
                if char != "}":
                    return False
            if cur == "(":
                if char != ")":
                    return False
    if stack:
        return False
    return True

expr = "{asd()dfs}sd[]"
if areBracketsSame(expr):
    print("balanced")
else:
    print("not balanced")