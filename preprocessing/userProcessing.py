from tqdm import tqdm

from utils.objectSaver import save


def process_user_data(userPath):
    userDict = {}
    with open(userPath, 'r') as userFile:
        for line in tqdm(userFile):
            firstCommaLoc = line.find(',')
            userId = line[:firstCommaLoc]
            userData = line[(firstCommaLoc + 1):]
            if userId in userDict:
                userDict[userId].append(userData)
            else:
                userDict.update({userId : [userData]})
    save('data/outData/userDict.sav', userDict)
    while True:
        i = int(input("id: "))
        print(userDict[i])
