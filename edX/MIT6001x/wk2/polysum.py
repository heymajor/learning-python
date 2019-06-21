import math

def polysum( n , s ):

	area = (0.25 * n * s**2) / ( math.tan ( math.pi / n ))
	perimeter = n * s

	solution = area * perimeter**2
	return round( solution, 4 )





print(polysum( 86, 16))  # 2043979.0482