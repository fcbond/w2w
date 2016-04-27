###
### Very simple word for word translator
### * take a sentence in Chinese
### * tokenize it
### * translate the words
###
from collections import defaultdict as dd

test = '我吃了饭.'
zh2en = dd(lambda: '?')
zh2en['我'] = 'I'
zh2en['吃'] = 'eat' 
zh2en['饭'] = 'rice'
zh2en['.'] = '.'

def tokenize(sent):
    'stupid tokenizer'
    return list(test)

def translate(sent, dct):
    translated = []
    for w in tokenize(sent):
        translated.append(dct[w])
    return translated

print(translate(test,zh2en))

