'''
Problem Statement : Cyclic Shifts
Link : https://www.hackerearth.com/challenges/competitive/april-circuits-20/algorithm/lets-shift-2-36d90caa/
score : accepted
'''

import numpy
for _ in range(int(input())):
    N,m,c = input().split()
    N = int(N)
    m = int(m)
    if c=='L':
        N = numpy.binary_repr(N,16)
        new = N[m:]+N[:m]
        print(int(new,2))
    else:
        N = numpy.binary_repr(N,16)
        new = N[-m:]+N[:-m]        
        print(int(new,2))
        

