import compas
import compas.datastructures as cd

mesh = cd.Mesh.from_obj(compas.get('hypar.obj'))

# display
if compas.is_rhino():
    import compas_ghpython.artists as artist
    a = artist.MeshArtist(mesh).draw()

else:
    from compas_view2.app import App
    viewer = App()
    viewer.add(mesh)
    viewer.run()
    mesh.to_json("output.json")
