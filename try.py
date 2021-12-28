def areBracketsBalanced(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        elif char not in [")", "}", "]"]:
            # means its a letter and not a bracket so do nothing
            None
        else:
            if not stack:
                return False
            # its opposite bracket.
            current_char = stack.pop()
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    if stack:
        return False
    else:
        return True


if __name__ == '__main__':
    expr = "{asd()dfs}sd[]"
    if areBracketsBalanced(expr):
        print("balanced")
    else:
        print("not balanced")
