import re

classes = [ 'axe deo',
            'best-seller books',
            'calvin klein',
            'camcorder',
            'camera',
            'chemistry',
            'chromebook',
            'c programming',
            'data structures algorithms',
            'dell laptops',
            'dslr canon',
            'mathematics',
            'nike-deodrant',
            'physics',
            'sony cybershot',
            'spoken english',
            'timex watch',
            'titan watch',
            'tommy watch',
            'written english']

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

def preprocess_line(line):
	# split line into tokens
	tokens = line.split('\t')
	# get data tokens
	_result = tokens[0]
	query = tokens[1]

	# process result
	result = process_sentence(_result)

	return result, query

# find longest common sub-sequence of 2 strings
def lcs(result, query, m, n):
    if m < 0 or n < 0:
        return 0

    if result[m] == query[n]:
        return 1 + lcs(result, query, m-1, n-1)

    return max(lcs(result, query, m-1, n), lcs(result, query, m, n-1))
