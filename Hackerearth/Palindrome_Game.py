'''
    Problem Statement : Palindrome Game
    Link : https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/palindrome-game-dcf03e89/
    score : 16.5
'''

string = input()
player = 0
box = dict()
unique = set(string)
for j in unique:
    box[j] = 0

player = -1  
string = list(string)
try:
    while string:
        if box[string[-1]]==0:
            box[string[-1]] += 1
            string.pop(-1)
            player += 1 
        if box[string[0]]==0:
            box[string[0]] += 1
            string.pop(0)
            player += 1
        else:
            box[string[0]] += 1
            if player%2 == 1:
                print('Alice')
            else:
                print('Bob')
            break
except:
    pass
if not string:
    print('Tie')