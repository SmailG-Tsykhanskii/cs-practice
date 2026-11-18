import numpy as np

def make_hours():
	return np.arange(0,24,3)

def vector_report(values):
	return dict([('third',values[2]),('last',values[-1]),('middle',values[2:6]),('every_second',values[::2]),('reversed',values[::-1])])

def change_vector(values):
	a = values.copy()
	a[1:4] = 99
	a[5::2] = -1
	return a

def cap_above(values, limit):
	a = values.copy()
	a[a > limit] = limit
	return a

def celsius_to_fahrenheit(values):
	return values * 9 / 5 + 32
