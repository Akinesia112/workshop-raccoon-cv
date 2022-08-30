"""Example: transform point and vector
"""
from compas.geometry import Point
from compas.geometry import Vector
from compas.geometry import Rotation

# create Rotation around point with axis and angle
point = cg.Point(1.0, 0.0, 0.0)
axis, angle = [-0.248, -0.786, -0.566], 2.78
R = Rotation.from_axis_and_angle(axis, angle, point=point)

# apply Transformation to Point
p = cg.Point(1, 1, 1)
p.transform(R)

# apply Transformation to Vector
v = cg.Vector(1, 1, 1)
v.transform(R)

# should not be the same!
print(repr(p))
print(repr(v))
