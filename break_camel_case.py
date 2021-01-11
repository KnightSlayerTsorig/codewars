# Complete the solution so that the function will break up camel casing, using a space between words.


def solution(s):
    new_s = []
    for el in s:
        if el == el.upper():
            el = ' ' + el
            new_s.append(el)
        else:
            new_s.append(el)

    s = ''.join(new_s)
    return s

