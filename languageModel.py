# import keras

text = 'Instead of defining the complete probability distribution over words, the model learns to differentiate between the correct training pairs retrieved from the corpus and the incorrect, randomly generated pairs. For each correct pair the model draws m negative ones — with m being a hyperparameter. All negative samples have the same Vt as the original training pair, but their Vc is drawn from an arbitrary noise distribution. Building on the previous example, for the training pair (prickles, nose) the incorrect ones could be (prickles, worked) or (prickles, truck). The new objective of the model is to maximise the probability of the correct samples coming from the corpus and minimise the corpus probability for the negative samples, such as (prickles, truck).'

import re
import numpy as np

def clean_word(word):
    alphaWord = re.sub(r'[^a-zA-Z]', '', word)
    return alphaWord.lower().strip()

def make_word_vec(wordIdx, vocabSize):
    wordVec = np.zeros(shape=(vocabSize,))
    wordVec[wordIdx] = 1
    return wordVec

cleanWords = set(map(lambda word : clean_word(word), text.split()))
vocabSize = len(cleanWords)
idxWordDict = {i : word for i, word in enumerate(cleanWords)}
oneHotWordDict = {word : make_word_vec(wordIdx, vocabSize)
                    for wordIdx, word in idxWordDict.items()}

for sentence in text.split('.'):
    
