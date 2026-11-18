import numpy as np

def make_hours():
	return np.arange(0,24,3).tolist()

def vector_report(values):
	return dict([('third',values[2]),('last',values[-1]),('middle',values[2:6]),('every_second',values[::2]),('reversed',values[::-1])])

def change_vector(values):
	a = np.asarray(values).copy()
	a[2:4] = 99
	a[::2] = -1
	return a.tolist()

def cap_above(values, limit):
	a = np.asarray(values).copy()
	a[a > limit] = limit
	return a.tolist()

def celsius_to_fahrenheit(values):
	return (np.asarray(values) * 9 / 5 + 32).tolist()
print(celsius_to_fahrenheit(make_hours()))
