import re

# global variables
words = []

# random words + higher frequency words
male_words = ['he', 'him', 'himself', 'man', 'men', 'his', 'brother', 'businessman', 'father', 'boy', 'son', 'pop', 'pops', 'dad']
female_words = ['she', 'her', 'hers', 'herself', 'woman', 'women', 'hers', 'sister', 'businesswoman', 'mother', 'girl', 'daughter', 'mom', 'mommy', 'nurse']

male_prefix = ['mr']
female_prefix = ['miss', 'ms', 'mrs']


def process_sentence(sentence):
    # convert to lower
    line = sentence.lower()
    # remove extra spaces
    line = line.strip()
    # create a space between word and the punctuation following it
    # line = re.sub(r"([?.!,¿'])", r" \1 ", line)
    # replace everything with space except (a-Z, A-Z, 0-9)
    # that is remove all punctuations
    line = re.sub(r"[^a-zA-Z0-9]+", " ", line)
    # convert multiple spaces to a single space
    line = re.sub(r'[" "]+', " ", line)
    # remove extra spaces
    line = line.strip()

    # return the line
    return line


def load_corpus(filename):
    file = open(filename)

    lines = []

    for line in file:
        l = process_sentence(line)
        if l != ' ' or l != '\n':
            lines.append(l)


    for line in lines:
        for word in line.split(' '):
            words.append(word)

# iterates over whole document for every word
# definitely not optimised
# @TODO: use a mapping of words to their indices to get the index of proper words in O(1)
def get_prediction(name):
    len_to_check = 100
    score = 0
    for i, word in enumerate(words):
        if word == name:
            temp_score = 0
            s = i+1
            e = min(i + len_to_check, len(words))
            words_to_check = words[s:e]
            if words[i-1] in male_prefix:
                temp_score += 100
            elif words[i-1] in female_prefix:
                temp_score -= 100
            elif 'dr' in words[i-1].lower():
                temp_score += 20

            for w in words_to_check:
                if w in male_words:
                    temp_score += 6
                if w in female_words:
                    temp_score -= 6
                    
            score += temp_score

    return score


if __name__ == '__main__':
    load_corpus('corpus.txt')
    N = int(input())

    names = []

    for i in range(N):
        names.append(input().lower())

    for name in names:
        score = get_prediction(name)
        if score >= 0:
            print('Male')
        else:
            print('Female')

