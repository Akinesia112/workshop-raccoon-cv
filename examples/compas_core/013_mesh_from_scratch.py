import compas
import compas.datastructures as cd

mesh = cd.Mesh()

a = mesh.add_vertex()         # x,y,z coordinates are optional and default to 0,0,0
b = mesh.add_vertex(x=1)
c = mesh.add_vertex(x=1, y=1)
d = mesh.add_vertex(y=1)

mesh.add_face([a, b, c, d])

print(mesh.summary())

# display
if compas.is_rhino():
    import compas_ghpython.artists as artist
    a = artist.MeshArtist(mesh).draw()

else:
    from compas_view2.app import App
    viewer = App()
    viewer.add(mesh)
    viewer.run()
