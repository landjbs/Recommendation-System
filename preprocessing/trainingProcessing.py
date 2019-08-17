"""
Processes training data files
"""

def process_training_file(trainFilePath):
    """
    Maps users to time-sorted list of the movies they have rated and the rating
    they have given them
    """
    with open(trainFilePath, 'r') as trainFile:
        
