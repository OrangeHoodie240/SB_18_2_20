def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    stack = []
    for char in parens:
        if(char == '('):
            stack.append(char)
        else:
            if(len(stack) == 0 or stack[-1] != '('):
                return False
            else:
                stack.pop() 
    if(len(stack) != 0):
        return False
    return True