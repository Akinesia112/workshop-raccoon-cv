"""Example: Create a rotation from and axis and an angle.
"""
import compas.geometry as cg


aav = cg.Vector(-0.043, -0.254, 0.617)
angle, axis = aav.unitized(), aav.length
print(repr(angle), repr(axis))

R = cg.Rotation.from_axis_angle_vector(aav)
axis, angle = R.axis_and_angle
print(repr(axis), repr(angle))
