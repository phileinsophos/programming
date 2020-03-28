'''
    Problem Statement : Annoying Chemistry
    Link : https://www.hackerearth.com/challenges/competitive/march-circuits-20/algorithm/annoying-chemistry-f5fb9556/
    score : 80pts - partially accepted
'''
x,y,p,q = input().split()
x = int(x)
y = int(y)
p = int(p)
q = int(q)
answers = []
RHS_coeff = 1
    
while True:
    RHS = RHS_coeff*p + RHS_coeff*q
    RHS_c_atoms = RHS_coeff*p
    RHS_h_atoms = RHS_coeff*q
    
    LHS_c_coeff = RHS_c_atoms //x
    LHS_h_coeff = RHS_h_atoms //y
            
    
    LHS = LHS_c_coeff*x + LHS_h_coeff*y
    if RHS==LHS:
        print(f'{LHS_c_coeff} {LHS_h_coeff} {RHS_coeff}')
        break
        
    RHS_coeff += 1

