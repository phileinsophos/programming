'''
    Problem Statement : Going to Office
    Link : https://www.hackerearth.com/practice/basic-programming/operators/basics-of-operators/practice-problems/algorithm/going-to-office-e2ef3feb/description/
    score : 5
'''

D = int(input())
O = list(map(int,input().split(" ")))
C = list(map(int,input().split(" ")))
Oc = O[0]
Of = O[1]
Od = O[2]
Cs = C[0]
Cb = C[1]
Cm = C[2]
Cd = C[3]

online = int(Oc + (D-Of)*Od)
offline = int(Cb + (D/Cs)*Cm + D*Cd)

if online<offline or online == offline:
    print("Online Taxi")
else:
    print("Offline Taxi")

print(online,'--',offline)