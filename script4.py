def finsert(l, i, e):
    return l.insert(i, e)


def fprint(l):
    print(l)


def fremove(l, e):
    return l.remove(e)


def fappend(l, e):
    return l.append(e)


def fsort(l):
    return l.sort()


def fpop(l):
    return l.pop()


def freverse(l):
    return l.reverse()


myList = list()
n = int(input())
for x in range(n):
    comList = [item for item in input().split()]
    eval('f' + comList[0] + '(' + 'myList' + ',' + ', '.join(map(str, comList[1:])) + ')')
