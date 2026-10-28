import numpy as np

def reshape_rows(values, width):
	if len(values)%width==0:
		return np.asarray(values).reshape(len(values)//width,width).tolist()
	else:
		return []

def block(matrix, rows, columns):
	return np.asarray(matrix)[np.ix_(rows,columns)].tolist()
	
def column_means(matrix):
	if matrix!=[]:
		return np.mean(np.asarray(matrix),axis=0).tolist()
	else:
		return []
	
def column_range(matrix,column):
	if matrix!=[]:
		return float((np.amax(np.asarray(matrix),axis=0)-np.amin(np.asarray(matrix),axis=0))[column])
	else:
		return 0.0
