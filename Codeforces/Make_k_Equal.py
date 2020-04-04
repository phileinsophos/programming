'''
    Problem Statement : Make k Equal
    Link : https://codeforces.com/contest/1328/problem/F
    score : TLE 
'''
N,K = list(map(int,input().split()))
numbers = list(map(int,input().split()))
numbers.sort()
average = sum(numbers)//len(numbers)
steps_list = []
for n in numbers:
    steps_list.append([n,abs(n-average)])
steps = 0
temp = steps_list.copy()
for index,element in enumerate(temp):
        if element[1]==0:
            steps_list.remove(element)
            K -= 1

while True:
    while True:
        if steps_list[0][1] == 0:
            K -= 1
            steps_list.pop(0)
            break
        else:
            steps_list[0][1] -= 1
            steps += 1
            
    while True:
        if steps_list[-1][1] == 0:
            K -= 1
            steps_list.pop()
            break
        else:
            steps_list[-1][1] -= 1
            steps += 1
    if not K:
        break
            
print(steps)
        



