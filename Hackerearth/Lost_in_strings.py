'''
    Problem Statement : Lost in strings
    Link : https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/lost-in-strings-11fa4a5d/description/
    score : partially accepted
'''

data = list()
s = input()
data.append(s)
query = int(input())
for i in range(query):
    inp_data = list(input().split(" "))
    p = int(inp_data[1])
    n = int(inp_data[2])
    condition = int(inp_data[0])
    if condition==1:
        data.append(data[n-1][:p-1]+inp_data[3])
    elif condition==2:
        data.append(data[n-1][:p])
    else:
        answer = [True for word in data[p-1:n] if inp_data[3] in word]
        answer = set(answer)
        if True in answer:
            print("yes")
        else:
            print("no")