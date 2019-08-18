import matplotlib.pyplot as plt

from utils.objectSaver import load

userDict = load('data/outData/userDict_1.sav')
movieDict = load('data/outData/movieDict.sav')

lenList = []
for user, userObj in userDict.items():
    lenList.append(len(userObj.ratingList))

import numpy as np

print(max(lenList))
print(min(lenList))
print(np.mean(lenList))
