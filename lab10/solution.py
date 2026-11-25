import numpy as np

def make_table(rows, columns):
	return np.arange(0,rows*columns).reshape(rows,columns).tolist()
	
def rectangle(matrix, row_start, row_stop, column_start, column_stop):
	return np.array([x[column_start: column_stop] for x in np.array(matrix)[row_start:row_stop]]).tolist()

def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
	m = np.array(matrix.copy())
	for i in range(row_start, row_stop):
		for j in range(column_start, column_stop):
			m[i,j] = value
	return m.tolist()
	
def matrix_vector_product(matrix,vector):
	return (np.array(matrix) @ np.array(vector)).tolist()
	
def matrix_multiply(left,right):
	return (np.array(left) @ np.array(right)).tolist()

def transpose_matrix(matrix):
	return np.transpose(matrix).tolist()
	
def solve_system(matrix,vector):
	return np.linalg.solve(matrix, vector).tolist()

def tensor_channel_mean(tensor):
	return np.average(tensor, axis=-1).tolist()

def point_distance(first, second):
	return np.linalg.norm(np.array(first)-np.array(second))

