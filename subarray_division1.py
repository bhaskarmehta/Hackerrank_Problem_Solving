def birthday(s, d, m):
    # Write your code here
    count=0
    j=0
    sum=0
    if len(s)==1:
        sum=s[0]
        if d==sum:
            count+=1
    for i in range(0,m):
        sum+=s[i]
    if sum==d:
        count+=1
    for i in range(m,len(s)):
        sum=sum-s[i-m]+s[i]
        if sum==d:
            count+=1
    return count
s=[2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]

birthday(s, 18, 7)