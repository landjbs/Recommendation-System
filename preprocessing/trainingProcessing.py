"""
Processes training data files
"""

from tqdm import tqdm

from dataStructures.userObject import User
from dataStructures.ratingObject import RatingInstance
from utils.objectSaver import save

def process_training_file(trainFilePath, outPath=None):
    """
    Maps users to time-sorted list of the movies they have rated and the rating
    they have given them
    """
    with open(trainFilePath, 'r') as trainFile:
        # initialize dictionary to map user ids to User() objects
        userDict = {}
        for line in tqdm(trainFile):
            # line either caches movie id for ratings or declares rating
            if line.endswith(':\n'):
                # pull out the name of the movie
                curMovieId = line[:-2]
            else:
                # unpack rating declaration
                userId, rating, dateString = line.split(',')
                # build rating object of current instance
                currentRatingObj = RatingInstance(movieId=curMovieId,
                                                    userId=userId,
                                                    dateString=dateString,
                                                    rating=rating)
                # update User() obj of userId in userDict with current rating
                if userId in userDict:
                    userDict[userId].add_rating(currentRatingObj)
                else:
                    userDict.update({userId : User(id=userId)})
                    userDict[userId].add_rating(currentRatingObj)

    # sort User() objects in userDict by rating
    try:
        for userObject in userDict:
            userObject.sort(axis='rating')
    except Exception as e:
        print(f'Error: {e}')

    if outPath:
        save(userDict, outPath)

    return userDict
