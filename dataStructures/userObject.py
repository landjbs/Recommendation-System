"""
Defines user object to store data about a specific user's preferences
"""

class User():
    def __init__(self, id):
        self.id = id
        self.averageScore = None
        self.ratingList = []

    def add_rating(self, ratingObj):
        self.ratingList.append(ratingObj)

    def sort_ratings(self, axis):
        cleanAxis = axis.lower().strip()
        if (cleanAxis =='date'):
            get_score = lambda ratingObj : ratingObj.date
        elif (cleanAxis == 'rating'):
            get_score = lambda ratingObj : ratingObj.rating
        else:
            raise ValueError('Axis must be either "date" or "rating".')
        self.ratingList.sort(reverse=True, key=get_score())
