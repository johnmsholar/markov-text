from collections import defaultdict
import random

def generate_array_from_file(file_name):
    with open(file_name) as f:
        text = f.read()
    return text.split()

def generate_markov_model(words, gram_size):
    result = defaultdict(list)
    for index, word in enumerate(words):
        if index + gram_size >= len(words):
            current_gram = tuple(words[index: len(words)] + words[:index + gram_size - len(words)])
            next_word = words[index+gram_size - len(words)]
        else:
            current_gram = tuple(words[index:index+gram_size])
            next_word = words[index+gram_size]
        result[current_gram].append(next_word)
    return result

def generate_text_from_model(model, length):
    result = ''
    current_gram = random.choice(model.keys())
    result += reduce(lambda a, b: a + ' ' + b, list(current_gram))
    for i in range(length):
        next_word = random.choice(model[current_gram])
        result += next_word + ' '
        current_gram = tuple(list(current_gram)[1:] + [next_word])
    return result

file_name = 'harrypotter2.txt'
gram_size = 2
output_length = 100
words = generate_array_from_file(file_name)
markov_model = generate_markov_model(words, gram_size)
print generate_text_from_model(markov_model, output_length)