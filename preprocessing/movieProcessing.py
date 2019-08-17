"""
Converts each movie into a one hot encoded title
"""

import pandas as pd

prevNum = 0
with open('data/inData/movie_titles.txt', 'r') as movieFile:
    for line in movieFile:
        print(line)
