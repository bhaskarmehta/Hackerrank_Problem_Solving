def saveThePrisoner(n, m, s):
    # Write your code here
    return (m-1+s)%n or n
print(saveThePrisoner(7,19,2))