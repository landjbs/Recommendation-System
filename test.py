import matplotlib.pyplot as plt

from utils.objectSaver import load

userDict = load('data/outData/userDict_1.sav')
movieDict = load('data/outData/movieDict.sav')

lenList = []
count = 0
for user, userObj in userDict.items():
    curLen = len(userObj.ratingList)
    if curLen > 300:
        print(curLen)
        count += 1
    lenList.append(curLen)

print(count)
import numpy as np

print(max(lenList))
print(min(lenList))
print(np.mean(lenList))
