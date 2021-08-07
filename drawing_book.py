def pageCount(n, p):
    # Write your code here
    if(p-1)<(n-p):
        return p//2
    else:
        if n%2==0:
                return ((n-p)+1)//2
        else:
                return (n-p)//2
print(pageCount(7,2))