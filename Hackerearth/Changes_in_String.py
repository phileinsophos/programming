'''
Problem Statement : Changes in String
Link : https://www.hackerearth.com/challenges/competitive/april-circuits-20/algorithm/ab-string-5f6b213a/
score : 
'''

def get_count(string):
    size = len(string)
    mid = 0
    count = 0
    if size %2==0:
        mid = size//2
    else:
        mid = (size//2)+1
    if size!=1:
        count = string[:mid].count('B')
    else:
        count = 0
        
    if string[mid+1:].count('A'):        
        count = count + get_count(string[mid+1:])
    return count
    
for _ in range(int(input())):
    size = int(input())
    string = list(input())
    mid = 0
    count = 0
    if size %2==0:
        mid = size//2
    else:
        mid = (size//2)+1
    if string.count('A'):
        count = string[:mid].count('B')
    else:
        count = 0
        
    if string[mid+1:].count('A'):        
        count = count + get_count(string[mid:])
    print(count)
    

