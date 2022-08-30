"""Example: Bring a box from the world coordinate system into another coordinate system.
"""
import compas
import compas.geometry as cg

# Box in the world coordinate system
frame = cg.Frame([1, 0, 0], [-0.45, 0.1, 0.3], [1, 0, 0])
width, length, height = 1, 1, 1
box = cg.Box(frame, width, length, height)

# Frame F representing a coordinate system
F = cg.Frame([2, 2, 2], [0.978, 0.010, -0.210], [0.090, 0.882, 0.463])

# Represent box frame in frame F and construct new box
box_frame_transformed = F.to_world_coordinates(box.frame)
box_transformed = cg.Box(box_frame_transformed, width, length, height)
print("Box frame transformed:", repr(box_transformed.frame))

if compas.is_rhino():
    import compas_ghpython.artists as artist
    a = (artist.FrameArtist(frame).draw(),
         artist.BoxArtist(box).draw(),
         artist.FrameArtist(F).draw(),
         artist.FrameArtist(box_frame_transformed).draw(),
         artist.BoxArtist(box_transformed).draw((0.2, 0., 0.2))
         )

else:
    from compas_view2.app import App
    viewer = App()
    viewer.add(frame)
    viewer.add(box)
    viewer.add(F)
    viewer.add(box_frame_transformed)
    viewer.add(box_transformed, color=(0.2, 0., 0.2), opacity=0.5)
    viewer.run()
