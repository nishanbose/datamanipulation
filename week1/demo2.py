def unique_counts(words):
	_words=set(words)
	_dict = dict( [ (a, words.count(a)) for a in _words ] )
	_result = sorted(_dict.items(), key = lambda words: _dict[1], reverse=True)
	return _result

print unique_counts(['Aurora', 'Jasmine', 'Jasmine', 'Jasmine', 'Belle', 'Belle'])