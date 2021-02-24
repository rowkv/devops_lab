lowUp = [int(x) for x in input().split()]
finalList = list()
for i in range(lowUp[0], lowUp[1] + 1):
    myList = [x for x in str(i)]
    s = 0
    for item in myList:
        if not int(item) == 0:
            s += int(i) % int(item)
        else:
            s += 1
    if s == 0:
        finalList.append(int(i))
print(finalList)
