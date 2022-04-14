'''
    Remove the numbers that appear more than once.
'''


def remove(l): 
    i = 0
    while i < len(l):
        j = 0
        while j < len(l):
            if i != j:
                if l[i] == l[j]:
                    l.pop(j)
                    n -= 1
            j += 1
        i += 1
    return l
