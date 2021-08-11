def viralAdvertising(n):
    # Write your code here
    comulative=0
    shared=5
    while(n!=0):
        liked=shared//2
        shared=3*liked
        comulative+=liked
        n-=1
    return comulative
print(viralAdvertising(5))