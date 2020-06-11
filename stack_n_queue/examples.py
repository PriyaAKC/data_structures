# Balanced Parenthesis
"""
Determine whether a string has balanced parentheses, using stack
Example:
Balanced: (), {()}, [[{()}]]
Non-balanced: {[)], {(), [][]}}
"""

from stack_n_queue import Stack


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paran_balanced(paren_string):
    paren_stack = Stack()
    for s in paren_string:
        if s in "({[":
            paren_stack.push(s)
        elif s in ")}]":
            if paren_stack.is_empty():
                return False
            else:
                top = paren_stack.pop()
                if not is_match(top, s):
                    return False
    if paren_stack.is_empty():
        return True

# Test many cases
print(is_paran_balanced("{})"))