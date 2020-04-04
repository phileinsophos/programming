'''
    Problem Statement : Helpful Maths
    Link : https://codeforces.com/problemset/problem/339/A
    score : accepted
'''
string = input().split('+')
if len(string) > 1:
    operands = []
    operands = [int(index) for index in string]
    operands.sort()
    operands = [str(x) for x in operands]
    print('+'.join(operands))
else:
    print(*string)

