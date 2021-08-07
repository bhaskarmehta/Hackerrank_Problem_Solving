def migratoryBirds(arr):
    # Write your code here
    """
    count=0
    index=0;
    max=0
    arr.sort()
    l=[]
    sum=0
    for i in range(1,6):
        count=0
        for j in range(0,len(arr)):
            if i==arr[j]:
                count+=1
        l.append(count)
    """
    max=0
    index=0
    l=[0,0,0,0,0]
    for i in range(0,len(arr)):
        l[arr[i]-1]+=1

    print(l)
    for i in range(0,5):
        if(l[i]>max):
            max=l[i]
            index=i

    print("max_frequency_element",index+1)
    """
    max1=max(l)
    for k in range(0,max1):
        sum+=l[k]
    print(max1)
    print(arr[sum-1])
    """
arr1=[1 ,2 ,3 ,4 ,5 ,4 ,3 ,2 ,1, 3 ,4]
arr=[1 ,4 ,4 ,4 ,5 ,3]

migratoryBirds(arr1)