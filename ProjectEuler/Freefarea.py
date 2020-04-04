'''
    Problem : 769
    Problem Statement : Freefarea
    Link : https://projecteuler.net/problem=679

'''
from itertools import product
S = ['A','E','F','R']
keywords = ['FREE','FARE','AREA','REEF']
file = open('outputs_generated.txt','a')
comb = product(S,repeat=15)
found = True
count = 0
total_words = 0
for word in comb:
    total_words += 1
    word = ''.join(word)
    for key in keywords:
        if key not in word:
            found = False
            break
        
    if found:
        key1 = word.count(keywords[0])
        key2 = word.count(keywords[1])
        key3 = word.count(keywords[2])
        key4 = word.count(keywords[3])
        if key1 == 1 and key2 == 1 and key3 == 1 and key4 == 1:
            file.write(word+'\n')
            count += 1
    found = True
file.close()
print("Total Words : ",total_words)
print("Keywords Matched : ",count)

