def formingMagicSquare(a):
    # Write your code here
    l = []     # for magic array we have to remember "HEBCIGFAD" and assign the value from 1 to 9
                    # and generate 8 matrices as A B C  as 8 3 4
    sum1 = 0        #                            H I D     1 5 9
                                           #     G F E     6 7 2
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    sum6 = 0
    sum7 = 0
    sum8 = 0
    sum1 += abs(8 - a[0][0]) + abs(3 - a[0][1]) + abs(4 - a[0][2]) + abs(1 - a[1][0]) + abs(5 - a[1][1]) + abs(
        9 - a[1][2]) + abs(6 - a[2][0]) + abs(7 - a[2][1]) + abs(2 - a[2][2])
    l.append(sum1)

    sum2 += abs(8 - a[0][0]) + abs(1 - a[0][1]) + abs(6 - a[0][2]) + abs(3 - a[1][0]) + abs(5 - a[1][1]) + abs(
        7 - a[1][2]) + abs(4 - a[2][0]) + abs(9 - a[2][1]) + abs(2 - a[2][2])
    l.append(sum2)

    sum3 += abs(6 - a[0][0]) + abs(1 - a[0][1]) + abs(8 - a[0][2]) + abs(7 - a[1][0]) + abs(5 - a[1][1]) + abs(
        3 - a[1][2]) + abs(2 - a[2][0]) + abs(9 - a[2][1]) + abs(4 - a[2][2])
    l.append(sum3)

    sum4 += abs(6 - a[0][0]) + abs(7 - a[0][1]) + abs(2 - a[0][2]) + abs(1 - a[1][0]) + abs(5 - a[1][1]) + abs(
        9 - a[1][2]) + abs(8 - a[2][0]) + abs(3 - a[2][1]) + abs(4 - a[2][2])
    l.append(sum4)

    sum5 += abs(2 - a[0][0]) + abs(7 - a[0][1]) + abs(6 - a[0][2]) + abs(9 - a[1][0]) + abs(5 - a[1][1]) + abs(
        1 - a[1][2]) + abs(4 - a[2][0]) + abs(3 - a[2][1]) + abs(8 - a[2][2])
    l.append(sum5)

    sum6 += abs(2 - a[0][0]) + abs(9 - a[0][1]) + abs(4 - a[0][2]) + abs(7 - a[1][0]) + abs(5 - a[1][1]) + abs(
        3 - a[1][2]) + abs(6 - a[2][0]) + abs(1 - a[2][1]) + abs(8 - a[2][2])
    l.append(sum6)

    sum7 += abs(4 - a[0][0]) + abs(9 - a[0][1]) + abs(2 - a[0][2]) + abs(3 - a[1][0]) + abs(5 - a[1][1]) + abs(
        7 - a[1][2]) + abs(8 - a[2][0]) + abs(1 - a[2][1]) + abs(6 - a[2][2])
    l.append(sum7)

    sum8 += abs(4 - a[0][0]) + abs(3 - a[0][1]) + abs(8 - a[0][2]) + abs(9 - a[1][0]) + abs(5 - a[1][1]) + abs(
        1 - a[1][2]) + abs(2 - a[2][0]) + abs(7 - a[2][1]) + abs(6 - a[2][2])
    l.append(sum8)
    min1 = min(l)
    return min1
a=[[2,3,4],[5,4,6],[7,9,3]]
print(formingMagicSquare(a))