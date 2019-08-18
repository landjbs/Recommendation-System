"""
Defines user object to store data about a specific user's preferences
"""

import numpy as np

class User():
    def __init__(self, id):
        self.id = id
        self.averageScore = None
        self.ratingList = []

    def add_rating(self, ratingObj):
        """ Add rating object of a moive """
        self.ratingList.append(ratingObj)

    def sort_ratings(self, axis):
        cleanAxis = axis.lower().strip()
        if (cleanAxis =='date'):
            sort_key = lambda ratingObj : ratingObj.date
        elif (cleanAxis == 'rating'):
            sort_key = lambda ratingObj : ratingObj.rating
        else:
            raise ValueError('Axis must be either "date" or "rating".')
        self.ratingList.sort(reverse=True, key=sort_key)

    def calc_average_rating(self):
        get_rating = lambda ratingObj : ratingObj.rating
        ratingList = [get_rating(ratingObj) for ratingObj in self.ratingList]
        self.averageScore = np.mean(ratingList)
