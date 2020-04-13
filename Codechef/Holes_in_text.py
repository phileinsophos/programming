'''
Problem Statement : Holes in the text 
Link : https://www.codechef.com/problems/HOLES
score : accepted
'''
holes_letters = {
    'A':1,
    'B':2,
    'D':1,
    'O':1,
    'P':1,
    'R':1,
    'Q':1,
}

for _ in range(int(input())):
    string = input()
    holes = 0
    for letter in string:
        count = holes_letters.get(letter,0)
        holes += count
    print(holes)

