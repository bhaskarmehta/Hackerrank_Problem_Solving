def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    l = []
    for i in range(0, len(keyboards)):
        for j in range(0, len(drives)):

            if (keyboards[i] + drives[j]) <= b:
                l.append(keyboards[i] + drives[j])
    if len(l) == 0:
        return -1
    else:
        return max(l)
key=[3,1]
drives=[5,2,8]
print(getMoneySpent(key,drives,10))