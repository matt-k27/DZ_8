print('DZ8')

originalList = []

if originalList:
    rebuildList = originalList[::2]
    res = 0

    for k in rebuildList:
        res += k

    print(res*originalList.pop())
else:
    print(0)

# with SUM

originalList = []

if originalList:
    rebuildList = originalList[::2]

    print(sum(rebuildList)*originalList.pop())
else:
    print(0)

print('Thank you for using')