###
### Very simple word for word translator
### * take a sentence in Chinese
### * tokenize it
### * translate the words
###
from collections import defaultdict as dd
from chien.chien import cnendict_internal as cnendict



zh2en = dd(lambda: '‽')
zh2en['我'] = 'I'
zh2en['吃'] = 'eat'  
zh2en['饭'] = 'rice'
zh2en['.'] = '.'
zh2en.update(cnendict)

def tokenize(sent):
    'stupid tokenizer'
    return list(sent)

def translate(sent, dct):
    translated = []
    for w in tokenize(sent):
        translated.append(dct[w])
    return translated

def main():
    tests = ['我吃饭了.',
             '我打猫.',
             '狗溜猫',
             '狗喜欢猫']

    for test in tests:
        print(test)
        print(' '.join(translate(test,zh2en)))

if __name__ == "__main__":
    main()

