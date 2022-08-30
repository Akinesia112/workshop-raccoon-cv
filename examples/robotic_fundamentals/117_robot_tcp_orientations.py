"""Example: Different Robot vendors use different conventions to describe TCP orientation."""

import compas.geometry as cg

point = cg.Point(0.0, 0.0, 63.0)
xaxis = cg.Vector(0.68, 0.68, 0.27)
yaxis = cg.Vector(-0.67, 0.73, -0.15)
F = cg.Frame(point, xaxis, yaxis)

print(repr(F.quaternion))  # ABB
print(repr(F.euler_angles(static=False, axes='xyz')))  # Staubli
print(repr(F.euler_angles(static=False, axes='zyx')))  # KUKA
print(repr(F.axis_angle_vector))  # UR
