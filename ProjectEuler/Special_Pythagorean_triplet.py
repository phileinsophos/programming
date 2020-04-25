'''
Problem Statement : Special Pythagorean triplet
Link : https://projecteuler.net/problem=9
score : accepted 
'''
squares = []
number = 1
answer_found = True
while answer_found:
    number_square = number**2
    if number_square not in squares:
        squares.append(number_square)
    for sq in squares:
        second_number_square = number_square - sq
        if second_number_square in squares:
            a = int(sq**0.5)
            b = int(second_number_square**0.5)
            c = int(number_square**0.5)
            if a+b+c == 1000:
                print(a,' + ',b,' = ',c)
                print(a*b*c)
                answer_found = False 
                break
    number += 1
    

