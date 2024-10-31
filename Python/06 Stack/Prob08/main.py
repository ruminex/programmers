# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solution(s):
    stack = []
    for c in s:
        if (c == '('):
            stack.append(c)
        elif(c == ')'):
            if(len(stack) == 0):
                return False
            else:
                stack.pop()

    if(len(stack) == 0):
        return True
    else:
        return False

print(solution('(())()'))
print(solution('((())()'))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
