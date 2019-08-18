from preprocessing.movieProcessing import build_movie_dict

build_movie_dict('data/inData/movie_titles.txt',
                outPath='data/outData/movieDict.sav')


# from preprocessing.trainingProcessing import process_training_file
# process_training_file('data/inData/combined_data_1.txt',
                    # outPath='data/outData/userDict_1.sav')
