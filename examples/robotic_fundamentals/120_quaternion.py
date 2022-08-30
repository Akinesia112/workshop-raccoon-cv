"""Example: Create a rotation from a quaternion.
"""
import compas.geometry as cg


q = cg.Quaternion(0.918958, -0.020197, -0.151477, 0.363544)
print(q.is_unit)
R = cg.Rotation.from_quaternion(q)
print(R.quaternion == q)
