'''
    Problem Statement : Uncle Johny
    Link : https://www.codechef.com/problems/JOHNY
    Score : accepted
'''

for _ in range(int(input())):
    N = int(input())
    songs = list(map(int,input().split()))
    K_index = int(input())
    uncle_jonny = songs[K_index-1]
    songs.sort()
    print(songs.index(uncle_jonny)+1)