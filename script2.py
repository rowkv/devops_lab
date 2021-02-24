def comSort(l1, l2):
    return list(set(l1) & set(l2))


l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
print(*comSort(l1, l2))
if ' ' in rec:
   print('Error')
else:
    if not RepresentsInt(l1[1]):
        print('Error')
    else:
        for i in ['+', '-', '/', '*']:
            if i in l1[0]:
                l2 = [x for x in l1[0].split(i)]
                if RepresentsInt(l2[0]) and RepresentsInt(l2[1]):
                    print('Yes')
