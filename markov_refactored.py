import random
# occasional err explained here:
# https://stackoverflow.com/questions/18161513/python-empty-range-for-randrange-0-0-0-and-valueerrorempty-range-for-ra

txt = "for god so loved the world that he gave his only begotten son so that all that believe in him shall not perish but have everlasting life in the beginning was the word and the word was with god and the word was god jesus wept my god my god why have you forsaken me god said let there be light"

txt = [i for i in txt.split(' ') if i != '']
txt = [i.lower() for i in txt if i.isalpha()]

def Markov(data):
    markov = {i:[] for i in data}
    pos = 0
    while pos < len(data) - 1:
        markov[data[pos]].append(data[pos+1])
        pos += 1
        new = {k:v for k,v in zip(range(len(markov)), [i for i in markov])}
        length_sentence = random.randint(15, 20)
        seed = random.randint(0, len(new) - 1)
        sentence_data = [new[seed]]
        current_word = new[seed]

    while len(sentence_data) < length_sentence:
        next_index = random.randint(0, len(markov[current_word]) - 1)
        next_word = markov[current_word][next_index]
        sentence_data.append(next_word)
        current_word = next_word
    return ' '.join([i for i in sentence_data])

markov_txt = Markov(txt)
print(markov_txt)
