'''
    Problem Statement : Let's swap
    Link : https://www.hackerearth.com/challenges/competitive/october-easy-20/algorithm/lets-swap-5075ade8/
    Score : partially accepted - 12 pts
'''

def get_beautifullness(numbers):
    return (sum([ abs(element-(i+1)) for i,element in enumerate(numbers)]))


n = int(input())
p = list(map(int,input().split()))

temp = p.copy()
temp.sort(reverse=True)

start = 1
end = n

swap1=0
swap2=0
while(start < end):
    if p[start-1] - start == 0:
        swap1 = start-1
    
    if p[end-1] - end == 0:
        swap2 = end-1
    start += 1
    end -= 1

p[swap1], p[swap2] = p[swap2], p[swap1]
print(get_beautifullness(p))
