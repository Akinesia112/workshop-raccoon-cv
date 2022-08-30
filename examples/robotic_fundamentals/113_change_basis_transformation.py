"""Change-basis transformation.
"""
import compas.geometry as cg

F1 = cg.Frame.worldXY()
F2 = cg.Frame([1.5, 1, 0], [0.68, 0.68, 0.27], [-0.67, 0.73, -0.15])
P = cg.Point(2, 2, 2)  # local point in F1

# change-basis transformation between two frames F1 and F2.
T = cg.Transformation.from_change_of_basis(F1, F2)

# Represent geometry (=point P) in another coordinate frame
print(repr(P.transformed(T)))
# You can also use the following
print(repr(F2.to_local_coordinates(P)))
