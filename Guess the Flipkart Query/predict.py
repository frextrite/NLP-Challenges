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
	_result = tokens[0]
	query = tokens[1]

	# process result
	result = process_sentence(_result)
	query = query.strip()

	return result, query

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
