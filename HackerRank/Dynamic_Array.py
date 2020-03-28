'''
    Problem Statement : Dynamic Array
    Link : https://www.hackerrank.com/challenges/dynamic-array/problem
    score : accepted
'''
def dynamicArray(n, queries):
    seqList = [[None]]*n
    answers = []
    lastAnswer = 0
    for q in queries:
        if int(q[0])==1:
            x = int(q[1])
            y = int(q[2])
            index = (x^lastAnswer)%n
            seq = seqList[index].copy()
            if None in seq:
                seq = [y]
            else:
                seq.append(y)
            seqList[index]=seq
        if int(q[0])==2:
            x = int(q[1])
            y = int(q[2])
            index = (x^lastAnswer)%n
            seq = seqList[index]
            value = y%len(seq)
            lastAnswer = seq[value]
            answers.append(lastAnswer)
    return answers


N,Q = input().split()
N = int(N)
Q = int(Q)
queries = []
for i in range(Q):
    queries.append(list(map(int,input().split())))
dynamicArray(N,queries)

