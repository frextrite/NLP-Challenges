import re

original_classes = [ 'axe deo',
			'calvin klein',
			'mathematics',
			'physics',
			'chemistry',
			'nike-deodrant',
			'camcorder',
			'camera',
			'chromebook',
			'data structures algorithms',
			'dell laptops',
			'dslr canon',
			'sony cybershot',
			'timex watch',
			'titan watch',
			'tommy watch',
			'written english',
			'spoken english',
			'best-seller books',
			'c programming']

classes = [ 'axe deo',
			'calvin klein',
			'mathematics',
			'physics',
			'chemistry chem chemical',
			'nike deodrant',
			'cam corder',
			'camera',
			'chromebook',
			'data structures algorithms',
			'dell laptops',
			'dslr canon',
			'sony cybershot',
			'timex watch',
			'titan watch',
			'tommy watch',
			'written english',
			'spoken english',
			'best seller books',
			'c programming']

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
	_sentence = tokens[0]

	# process result
	sentence = process_sentence(_sentence)

	return sentence

# find longest common sub-sequence of 2 strings
def lcs(dp, result, query, m, n):
	if m < 0 or n < 0:
		return 0

	if dp[m][n] != -1:
		return dp[m][n]

	if result[m] == query[n]:
		dp[m-1][n-1] = 1 + lcs(dp, result, query, m-1, n-1)
		return dp[m-1][n-1]

	dp[m-1][n] = lcs(dp, result, query, m-1, n)
	dp[m][n-1] = lcs(dp, result, query, m, n-1)

	return max(dp[m-1][n], dp[m][n-1])

def get_query(result):
	result_length = len(result)

	lcs_classes = []
	# iterate over every class and get scores based on context similarity
	for query_class in classes:
		# initialize dp state to -1
		dp = [[-1]*len(query_class) for i in range(result_length)]
		# initialize score adder to zero
		add = 0

		query_words_list = query_class.split(' ')

		for word in query_words_list:
			if word == 'c':
				word = 'c '
			if word in result:
				add += 100

		# if all the query words are present in the result
		# we have found a perfect match
		if int(add / 100) == len(query_words_list):
			lcs_classes.append(1000)
			return original_classes[classes.index(query_class)]
		else:
			score = add + lcs(dp, result, query_class, result_length-1, len(query_class)-1)
			lcs_classes.append(score)
			
	if 'paperback' in result.split(' ') and max(lcs_classes) < 100:
		return original_classes[18]
	
	return original_classes[lcs_classes.index(max(lcs_classes))]