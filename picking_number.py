def pickingNumbers(a):
    # Write your code here
    max1=0
    for i in a:
        c=a.count(i)
        d=a.count(i-1)
        e=c+d
        if e>max1:
            max1=e



    return max1


l=[4 ,6 ,5 ,3 ,3 ,1]
l1=[1 ,2 ,2 ,3 ,1 ,2]
l2=[66 ,66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66]
l3=[4, 2, 3, 4, 4, 9, 98, 98, 3, 3, 3, 4, 2, 98, 1, 98, 98, 1 ,1, 4, 98, 2, 98, 3, 9, 9, 3, 1, 4, 1, 98, 9, 9, 2, 9, 4,
    2, 2, 9, 98, 4 ,98, 1, 3, 4, 9, 1, 98, 98, 4, 2, 3, 98, 98, 1, 99, 9, 98, 98, 3, 98, 98, 4, 98, 2, 98, 4, 2, 1, 1, 9, 2, 4]
l4=[10,10,10,10]
print(pickingNumbers(l3))