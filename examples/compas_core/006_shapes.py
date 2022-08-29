import compas
import compas.geometry as cg

# Box
b1 = cg.Box(cg.Frame.worldXY(), 5, 1, 3)          # xsize, ysize, zsize
b2 = cg.Box.from_width_height_depth(5, 3, 1)   # width=xsize, height=zsize, depth=ysize
assert str(b1) == str(b2)
print(b1)

# Sphere
s1 = cg.Sphere([0, 0, 0], 5)
print(s1)

# Cylinder
plane = cg.Plane([0, 0, 0], [0, 0, 1])
circle = cg.Circle(plane, 5)
c1 = cg.Cylinder(circle, height=4)
print(c1)

# ==============================================================================
# Viz
# ==============================================================================
if compas.is_rhino():
    import compas_ghpython.artists as artist
    a = artist.ShapeArtist(b1).draw()

else:
    from compas_view2.app import App
    viewer = App()
    viewer.add(b1)
    viewer.run()