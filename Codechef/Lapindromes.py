'''
    Problem Statement : Lapindromes
    Link : https://www.codechef.com/LRNDSA01/problems/LAPIN
    score : accepted
'''
for _ in range(int(input())):
    string = input()
    mid = len(string)//2
    first_half = None
    second_half = None
    if len(string)%2==0:
        first_half = string[:mid]
        second_half = string[mid:]
    else:
        first_half = string[:mid]
        second_half = string[mid+1:]
        
    lapindrome = True
    char_first = set(first_half)
    char_second = set(second_half)
    if char_first == char_second:
        for ch in first_half:
            count_first = first_half.count(ch)
            count_second = second_half.count(ch)
            if count_first != count_second:
                lapindrome = False
                break
    else:
        lapindrome = False
    if lapindrome:
        print("YES")
    else:
        print("NO")

