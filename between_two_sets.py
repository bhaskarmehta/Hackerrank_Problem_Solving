def getTotalX(a, b):
    # Write your code here
    len1 = len(a)
    len2 = len(b)
    # std::cout<<"len1="<<len1<<"len2="<<len2;
    flag = 0
    count = 0
    for i in range(a[0], b[len2 - 1] + 1):

        # std::cout<<"\nfor i="<<i;
        flag = 0
        for j in range(0, len1):

            # std::cout<<"\ni="<<i<<" a[j]="<<a[j];
            if (i % a[j] != 0):
                flag = 1
            # std::cout<<"flag="<<flag;
        for k in range(0, len2):

            # std::cout<<"\nb[k]="<<b[k]<<" i="<<i;
            if (b[k] % i != 0):
                flag = 1
            # std::cout<<"flag="<<flag;

        if (flag == 0):
            count += 1
        # std::cout<<"/ncount="<<count;

    return count
a=[2,4]
b=[16,32,96]
print(getTotalX(a, b))
