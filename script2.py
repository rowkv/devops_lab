def comSort(l1, l2):
    return list(set(l1) & set(l2))


l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
print(*comSort(l1, l2))
