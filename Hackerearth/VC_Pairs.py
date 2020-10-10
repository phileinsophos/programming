'''
 
    Problem Statement : VC Pairs
    Link : https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/vc-pairs/submissions/
    Score : accepted
 
'''
for _ in range(int(input())):
    n = int(input())
    s = input()
    vowels ="aeiou"
    count = 0
    for index in range(len(s)-1):
        if(s[index] not in vowels):
            if(s[index+1] in vowels):
                count += 1
    print(count)