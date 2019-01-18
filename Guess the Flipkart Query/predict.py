import re

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

	print(result, '\t', query)
