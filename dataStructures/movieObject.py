"""
Class to store information about a movie
"""

class Movie():
    def __init__(self, id):
        self.id = id
        self.averageScore = None
        self.ratersList = []
