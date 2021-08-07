def breakingRecords(scores):
    # Write your code here
    max = scores[0]
    min = scores[0]
    count1 = 0
    count2 = 0
    for i in range(0, len(scores)):
        if max < scores[i]:
            max = scores[i]
            count1 += 1
        if min > scores[i]:
            count2 += 1
            min = scores[i]
    return count1, count2
l=[3 ,4 ,21 ,36 ,10 ,28 ,35 ,5 ,24 ,42]
print(breakingRecords(l))
