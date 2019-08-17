from tqdm import tqdm

from utils.objectSaver import save

def process_user_data(userPath):
    userDict = {}
    with open(userPath, 'r') as userFile:
        for line in tqdm(userFile):
            if ':' in line:
                print(line)
            else:
                firstCommaLoc = line.find(',')
                userId = line[:firstCommaLoc]
                userData = line[(firstCommaLoc + 1):]
                if userId in userDict:
                    userDict[userId].append(userData)
                else:
                    userDict.update({userId : [userData]})
    save(userDict, 'data/outData/userDict.sav')
    while True:
        i = (input("id: "))
        print(userDict[i])
