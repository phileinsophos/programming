'''
    Problem Statement : Sort an array of Strings according frequency

    Link : https://www.geeksforgeeks.org/sort-the-strings-according-to-its-frequency/

'''

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

def sort_strings(data):
    final_output = []
    string_dict = dict()
    for word in data:
            if string_dict.get(word):
                string_dict[word] += 1
            else:
                string_dict[word] = 1
    df = pd.DataFrame({'keys':list(string_dict.keys()),'values':list(string_dict.values())})
    counts = set(df['values'].to_list())
    for c in counts:
        filter = df['values'] == c
        temp = df.where(filter,inplace = False)
        temp = temp.dropna(axis=0)
        selected_strings = temp['keys'].to_list()
        selected_strings.sort()
        final_output.extend(selected_strings)
    print(final_output)
    
strings = ['abc', 'pqr', 'pqr', 'abc','zbc','zaq']
sort_strings(strings)

