def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    l1=len(apples)
    l2=len(oranges)
    count2=0
    count1=0


    for i in range(0,l1):
        if apples[i]+a>=s and apples[i]+a<=t:
            count1+=1
    for i in range(0,l2):
        if oranges[i]+b<=t and oranges[i]+b>=s:
            count2+=1
    print(count1)
    print(count2)

countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])