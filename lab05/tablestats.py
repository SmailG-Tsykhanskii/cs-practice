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
					row.append((names[j],A[j]))
			rows.append(dict(row))
	return rows

def count_types(rows):
        types = dict([(x['тип'],int()) for x in rows])
        for i in rows:
                types[i['тип']] += 1
        return types

