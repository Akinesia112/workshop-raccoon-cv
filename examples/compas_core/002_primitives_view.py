import compas
import compas.geometry as cg


# Point
point  = cg.Point(10, 10, 10)


# ==============================================================================
# Viz
# ==============================================================================
if compas.is_rhino():
    # in Grasshopper
    import compas_ghpython.artists as artist
    a = artist.PointArtist(point).draw()

else:
    from compas_view2.app import App
    viewer = App()
    viewer.add(point)
    viewer.run()