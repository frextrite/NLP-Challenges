import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def process_sentence(sentence):
    # convert to lower
    line = sentence.lower()
    # remove extra spaces
    line = line.strip()
    # create a space between word and the punctuation following it
    line = re.sub(r"([?.!,¿'])", r" \1 ", line)
    # replace everything with space except (a-Z, A-Z, 0-9)
    # that is remove all punctuations
    line = re.sub(r"[^a-zA-Z0-9]+", " ", line)
    # convert multiple spaces to a single space
    line = re.sub(r'[" "]+', " ", line)
    # remove extra spaces
    line = line.strip()

    # return the line
    return line


def return_corpus(sentence_list):
    corpus = set()
    for sentence in sentence_list:
        _sentence = process_sentence(sentence)
        for word in _sentence.split(' '):
            if word not in corpus:
                corpus.add(word)

    return corpus

def print_answer(vectorized_matrix):
    for description in vectorized_matrix[N:, :]:
        title = vectorized_matrix[:N, :]
        similarity = cosine_similarity(title, description)
        max_index = np.argmax(similarity)
        print(max_index+1)


if __name__ == '__main__':
    N = int(input())

    titles = []
    for i in range(N):
        titles.append(input())

    input()

    descriptions = []
    for i in range(N):
        descriptions.append(input())

    corpusA = return_corpus(titles)
    corpusB = return_corpus(descriptions)

    tfidf_vectorizer = TfidfVectorizer(ngram_range=(1,5), stop_words='english', max_df=0.5, norm='l2')

    vectorized_matrix = tfidf_vectorizer.fit_transform(titles + descriptions)

    print_answer(vectorized_matrix)
