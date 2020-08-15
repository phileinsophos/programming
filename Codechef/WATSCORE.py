'''
        Problem Statement : That Is My Score
        Link : https://www.codechef.com/DEC19B/problems/WATSCORE
        Score : 100

'''

test = int(input())
for t in range(test):
    submissions = int(input())
    data = {key:[0] for key in range(1,12)}
    for sub in range(submissions):
        pi,si = input().split(" ")
        pi = int(pi)
        si = int(si)

        data[pi].append(si)
    total = 0
    for sub in range(1,9):
        total += max(data[sub])
    print(total)
