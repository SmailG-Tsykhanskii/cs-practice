def read_rows(lines):
	rows = []
	names = []
	First = True
	for i in lines:
		if First:
			for j in map(str,i.split(',')):
				names.append(j)
			First = False
		elif len(i.split(','))==len(names):
			A = list(map(str,i.split(',')))
			row=[]
			for j in range(len(names)):
					rows.append({names[j],A[j]})
	return rows

print(['a,b','1,2'])
def count_types(rows):
	pass
	
