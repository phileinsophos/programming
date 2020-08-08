'''
    Problem Statement : Shuffle String
    Link : https://leetcode.com/contest/weekly-contest-199/problems/shuffle-string/
    Score : accepted
'''
class Solution:
    def restoreString(self, string: str, indices: List[int]) -> str:
        string_list = list(string)
        new_string = [None]*len(indices)
        for index,number in enumerate(indices):
                new_string[number] = string_list[index]
        return "".join(new_string)

