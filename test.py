from utils.objectSaver import load

userDict = load('data/outData/userDict_1.sav')

for user, userObj in userDict.items():
    print(user)
    print
