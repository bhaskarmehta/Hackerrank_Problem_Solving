def angryProfessor(k, a):
    # Write your code here
    count=0
    for i in a:
        if i<=0:
            count+=1
    if count>=k:
        return "NO"
    else:
        return "YES"
k=3
a=[-1 ,-3 ,4 ,2]
print(angryProfessor(k,a))