"""
Converts each movie title into a one hot encoded vector
of length (number of movies) and builds dict mapping movie ids to movie
title for O(1) lookup.
"""

import numpy as np
import pandas as pd
from tqdm import tqdm

from utils.objectSaver import save


def build_movie_dict(moviePath, outPath=None):
    """ Builds dict mapping movie ids to movie titles """
    movieDict = {}
    with open(moviePath, 'r') as movieFile:
        for line in tqdm(movieFile):
            firstCommaLoc = line.find(',')
            movieId, movieInfo = line[:firstCommaLoc], line[(firstCommaLoc+1):]
            secondCommaLoc = movieInfo.find(',')
            movieTitle = movieInfo[(secondCommaLoc+1):]
            movieDict.update({movieId : movieTitle})
            
    if outPath:
        save(movieDict, outPath)

    return movieDict


def process_movie_titles(moviePath):
    with open(moviePath, 'r') as movieFile:
        # build empty vector with a zero for each movie
        emptyMovieVector = [0 for _ in movieFile]
        # reset iterator over movieFile
        movieFile.seek(0)
        for i, line in enumerate(movieFile):
            emptyMovieVector[i] = 1
            print(sum(emptyMovieVector))
