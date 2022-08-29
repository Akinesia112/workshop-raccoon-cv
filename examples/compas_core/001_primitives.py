import compas.geometry as cg

# Point, Vector & Plane
point = cg.Point(0, 0, 0)
vector = cg.Vector(0, 0, 1)
plane = cg.Plane(point, vector)
print(point)
print(vector)
print(plane)

# Frame
xaxis = [1, 0, 0]
yaxis = [0, 1, 0]
frame = cg.Frame(point, xaxis, yaxis)
print(frame)

# Polyline
p1 = [0, 0, 0]
p2 = [1, 0, 0]
p3 = [1, 1, 0]
p4 = [0, 0, 0]
polyline = cg.Polyline([p1, p2, p3, p4])
print(polyline)

# Polygon
polygon = cg.Polygon([p1, p2, p3])
print(polygon)
