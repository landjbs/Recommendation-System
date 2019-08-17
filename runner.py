# from preprocessing.movieProcessing import process_movie_titles

# process_movie_titles('data/inData/movie_titles.txt')

from utils.objectSaver import load

# userDict = load('data/outData/userDict.sav')
# print(userDict['262367'])
#
# while True:
#     i = input("id: ")
#     print(userDict[i])

from preprocessing.userProcessing import process_user_data

process_user_data('data/inData/combined_data_1.txt')
