"""
Class to store information about a rating instance
"""

# dates are defined with respect to 1980-00-00
FIRST_YEAR = 1980
FIRST_MONTH = 0
FIRST_DAY = 0


def covert_date_string(dateString):
    """
    Converts dateString from form 2005-03-17 to int of days since first date
    IN PROGRESS
    """
    # read date string into list of ints
    dateList = [int(dateSection) for dateSection in dateString.split('-')]
    assert (len(dateList)==3), 'Date cannot be read'
    # unpack dateList and find number of days from first date
    curYear, curMonth, curDay = dateList


class RatingInstance():
    def __init__(self, movieId, userId, dateString, rating):
        self.movieId = movieId
        self.userId = userId
        self.data = dateString
        self.rating = rating
