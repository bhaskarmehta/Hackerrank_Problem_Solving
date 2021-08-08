def climbingLeaderboard(ranked, player):
    # Write your code here
    l = []
    s = sorted(set(ranked), reverse=True)
    for i in player:
        s.append(i)
        s.sort(reverse=True)
        l.append(s.index(i) + 1)
    return l
l1=[100 ,100 ,50 ,40 ,40 ,20 ,10]
l2=[5 ,25 ,50, 120]
print(climbingLeaderboard(l1,l2))