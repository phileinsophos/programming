'''
    Problem Statement : Laddu
    Link : https://www.codechef.com/LRNDSA01/problems/LADDU
    score : accepted
'''
for _ in range(int(input())):
    activities, origin = input().split(" ")
    activities = int(activities)
    laddu = 0
    for a in range(activities):
        string = input()
        if 'CONTEST_WON' in string:
            laddu = laddu + 300
            if int(string.split(" ")[1])<20:
                laddu = laddu + (20 - int(string.split(" ")[1]))
        if 'TOP_CONTRIBUTOR' in string:
            laddu = laddu + 300
        if 'BUG_FOUND' in string:
            laddu = laddu + int(string.split(" ")[1])
        if 'CONTEST_HOSTED' in string:
            laddu = laddu + 50
    if origin == 'INDIAN':
        print(laddu//200)
    else:
        print(laddu//400)

