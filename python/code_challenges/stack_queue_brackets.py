import pytest
from data_structures.queue import Queue


def multi_bracket_validation(my_string):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]

    # Function to check parentheses

    stack = []
    for i in my_string:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

    # brackets = ['()', '{}', '[]']
    # while any(x in my_string for x in brackets):
    #     for br in brackets:
    #         my_string = my_string.replace(br, '')
    # return not my_string

    # open_tup = tuple('({[')
    # close_tup = tuple(')}]')
    # map = dict(zip(open_tup, close_tup))
    # queue = []
    #
    # for i in string:
    #     if i in open_tup:
    #         queue.append(map[i])
    #     elif i in close_tup:
    #         if not queue or i != queue.pop():
    #             return False
    # if not queue:
    #     return True
    # else:
    #     return False

