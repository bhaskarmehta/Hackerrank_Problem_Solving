def getTotalX(a, b):
    # Write your code here
    count = 0
    l1 = len(a) - 1
    n = a[l1]
    print(n)
    lst=[]
    for i in range(n, b[0] + 1):
        lst.append(i)
    print(lst)

    if a[l1] < b[0]:

        for j in range(0, len(a)):
            for i in range(0,len(lst)):
                
                    if b[j] % lst[i] == 0:
                        continue
                count+=1


    return count
l1=[2]
l2=[20 ,30, 12]
a=[100,99,98,97,96, 95, 94, 93, 92, 91]
b=[1 ,2, 3 ,4 ,5, 6, 7, 8, 9, 10]
a1=[1]
b1=[100]
a2=[1]
b2=[72,48]

print(getTotalX(a2,b2))