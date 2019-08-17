"""
Class to store information about a rating instance
"""

class RatingInstance():

    def __init__(self, movieId, userId, date, rating):
        self.movieId = movieId
        self.userId = userId
        self.data = date
        self.rating = rating
