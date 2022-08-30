"""Transformation between two frames.
"""
import compas.geometry as cg

F1 = cg.Frame.worldXY()
F2 = cg.Frame([1.5, 1, 0], [0.68, 0.68, 0.27], [-0.67, 0.73, -0.15])
P = cg.Point(2, 2, 2)  # local point in F1

# transformation between 2 frames F1, F2
T = cg.Transformation.from_frame_to_frame(F1, F2)

# Transform geometry (=point P) into another coordinate frame
print(repr(P.transformed(T)))
