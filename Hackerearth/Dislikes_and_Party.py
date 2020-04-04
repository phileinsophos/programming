'''
    Problem Statement : Dislikes and Party
    Link: https://www.hackerearth.com/problem/algorithm/dislikes-and-party-567b9605/
    score : 2.6pts - partially accepted - memory limit excedded
'''
number = int(input())
data_matrix = []
for i in range(10):
    data = list(map(int,input().split()))
    matrix.append(data)

data_matrix.sort(key = lambda x: x[0])
available = [ [i for i in range(1,number+1)] for j in range(1,number+1)]
    
for index,row in enumerate(data_matrix): 
        for element in range(1,len(row)):
            try:
                available[row[0]-1].remove(row[element])
                available[row[element]-1].remove(row[0])
            except:
                pass
    
people = []
for i in range(number):
        available[i].remove(i+1)
    
for index,row in enumerate(available):
        for i in row:
            if (index+1,i) and (i,index+1) not in people:
                people.append((index+1,i))
                
print(len(people))


# In[ ]:




