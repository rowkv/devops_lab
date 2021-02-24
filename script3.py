def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


rec = input()
l1 = [x for x in rec.split('=')]
if ' ' not in rec:
    if RepresentsInt(l1[1]):
        for i in ['+', '-', '/', '*']:
            if i in l1[0]:
                l2 = [x for x in l1[0].split(i)]
                if RepresentsInt(l2[0]) and RepresentsInt(l2[1]):
                    if eval(l2[0] + i + l2[1]) == int(l1[1]):
                        print('YES')
                    else:
                        print('NO')
else:
    print('ERROR')
