# note => build GUI for this -> if must use w/js/react whatever

from random import randint

def markov_txt_generator(text):
    text = [i.lower() for i in text if i.isalpha()]
    print(text)


txt = open("infinite_jest_excerpt.txt").read().split(' ')
markov_txt_generator(txt)
