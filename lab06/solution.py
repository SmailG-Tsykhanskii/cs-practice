def count_items(values):
	counter = {}
	for i in values:
		counter[i] = counter.get(i, 0) + 1 
	return counter

def unique_sorted(values):
	return sorted(set(values))
	
def common(first, second):
	return sorted(set(first) & set(second))

def only_in_first(first,second):
	return sorted(set(first)-set(second))

