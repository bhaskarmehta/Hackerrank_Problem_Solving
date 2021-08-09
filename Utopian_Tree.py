def utopianTree(n):
    # Write your code here
    print(n)
    max1=max(n)
    h=1
    l=[1]
    print(max1)


    for i in range(1,max1+1):
        if i%2==0:
            h+=1
            l.append(h)
            print(i)
        elif i%2==1:
            h*=2
            l.append(h)
            print(i)
    l1=[l[j] for j in n]

    for k in l1:
        print(k)

n=[0,1,4]
n1=[0,1,2,3,4,5]
print(utopianTree(n))
