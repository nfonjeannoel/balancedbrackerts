def areBracketsBalanced(expr):
    stack = []
    # expr = "{asd()dfs}sd[]"
    for char in expr:
        print(f"we are working wit {char}")
        if char in ["(", "{", "["]:
            # push element to start
            print(f"character is opening")
            stack.append(char)
            print(f"stack now is {stack}")
        elif char not in [")", "}", "]"]:
            # element is not opening or closing bracket. do nothing
            print(f" char is mot opening or closing it is {char}")
            None
        else:
            print(f"char is closing {char}")
            # if current char is not opening bracket then it should be closing
            if not stack:
                print("stack is empty")
                return False
            print(f" stack is {stack}")
            current_char = stack.pop()
            print(f" we poped {current_char} from stack")
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if stack:
        return False
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    expr = "{asd()dfs}sd[]"
    if areBracketsBalanced(expr):
        print("balanced")
    else:
        print("not balanced")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
