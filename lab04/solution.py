names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]

def winner(names: list, scores: list) -> str:
	maxsc = scores[0]
	maxnm = names[0]
	for i in range(1, len(names)):
		if scores[i] > maxsc:
			maxsc = scores[i]
			maxnm = names[i]
	return maxnm

def average(scores: list) -> float:
	if scores == []: 
		return 0.0
	else:
		return round(0+sum(scores)/len(scores),2)
