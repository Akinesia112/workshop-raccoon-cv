"""Example: Transform a point and invert the transformation
"""
import math
import compas.geometry as cg

p = cg.Point(3, 4, 5)
T = cg.Rotation.from_axis_and_angle([2, 2, 2], math.pi/4)

p.transform(T)  # transform Point p with T
print(repr(p))

Tinv = T.inverse()  # create inverse Transformation to T

p.transform(Tinv)  # transform Point p with inverse Transformation

# check if p has the same values as in the beginning
print(repr(p))  # == (3, 4, 5)

# Btw, what is the result of multiplying T with Tinv?
print(T * Tinv)
