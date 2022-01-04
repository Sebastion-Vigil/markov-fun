import random

def Markov(text_file): # txt file 2 parse
    with open(text_file) as f:
        data = f.read()

    data = [i for i in data.split(' ') if i != ''] # list of all words
    data = [i.lower() for i in data if i.isalpha()] # remove punctuation
    markov = {i:[] for i in data} # dict words as k & empty [] as v

    pos = 0
    # random length
    length_sentence = random.randint(15, 20)
    # create another dict for the seed to match up with
    new = {k:v for k,v in zip(range(len(markov)), [i for i in markov])}
    # random start point
    seed = random.randint(0, len(new) - 1)
    # use as first word as well as starting point
    sentence_data = [new[seed]] # 2 b returned as answer
    current_word = new[seed]
    # add a word to the word-key's list if it immediately follows that word
    while pos < len(data) - 1: # -1 bcuz need 2 add nxt word to word/key list ([])
        markov[data[pos]].append(data[pos+1])
        pos += 1

    while len(sentence_data) < length_sentence:
        # randomly pick word from the last word's list
        next_index = random.randint(0, len(markov[current_word]) - 1)
        next_word = markov[current_word][next_index]
        sentence_data.append(next_word)
        current_word = next_word

    return ' '.join([i for i in sentence_data])


markov_txt = Markov("infinite_jest_excerpt.txt")
print(markov_txt)