def hurdleRace(k, height):
    # Write your code here
    max1=0
    for i in height:
        if i>max1:
            max1=i
    h=max1-k
    if h>0:
        return h
    else:
        return 0
l=[2 ,5 ,4 ,5 ,2]
k=7
print(hurdleRace(k,l))