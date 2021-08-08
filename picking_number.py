def pickingNumbers(a):
    # Write your code here

    print(a)
    count = 1

    print(len(a))
    for i in range(0,len(a)):
        for j in range(i+1,len(a)-1):
            if(abs(a[i])-a[j])<=1:
                continue
            else:
                break



l=[4 ,6 ,5 ,3 ,3 ,1]
print(pickingNumbers(l))