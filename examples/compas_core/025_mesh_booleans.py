import compas
import compas.geometry as cg
from compas.datastructures import Mesh


b1 = cg.Box(cg.Frame([+4, +4, 0], [1, 0, 0], [0, 1, 0]), 10, 10, 10)
b2 = cg.Box(cg.Frame([-4, -4, 0], [1, 0, 0], [0, 1, 0]), 10, 10, 10)

A = Mesh.from_shape(b1)
B = Mesh.from_shape(b2)

A.quads_to_triangles()
B.quads_to_triangles()

A = A.to_vertices_and_faces()
B = B.to_vertices_and_faces()

# Use best boolean union available depending on context
V, F = cg.boolean_union_mesh_mesh(A, B)

mesh = Mesh.from_vertices_and_faces(V, F)
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