def countingValleys(steps, path):
    # Write your code here
    sea = 0
    valley = 0
    count = 0
    for i in range(0, steps):
        if sea == 0:
            if path[i] == 'D':
                valley += 1
        if path[i] == 'U':
            sea += 1
        if path[i] == 'D':
            sea -= 1

    return valley
l="UDDDUDUU"
print(countingValleys(8,l))