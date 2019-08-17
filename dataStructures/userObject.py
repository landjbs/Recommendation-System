"""
Defines user object to store data about a specific user's preferences
"""

class User():

    def __init__(self, id):
        self.id = id
        self.averageScore = None
        self.ratingList = []

    def add_rating(self, ratingObj):
        
