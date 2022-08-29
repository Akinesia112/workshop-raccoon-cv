import math
import compas
import compas.datastructures as cd
import compas.geometry as cg

# ==============================================================================
# Get Bunny
# ==============================================================================

before = cd.Mesh.from_ply(compas.get_bunny())

# ==============================================================================
# Clean up
# ==============================================================================

before.cull_vertices()

# ==============================================================================
# Transform
# ==============================================================================

T = cg.Translation.from_vector(cg.Point(0, 0, 0) - cg.Point(* before.centroid()))
S = cg.Scale.from_factors([100, 100, 100])
R = cg.Rotation.from_axis_and_angle([1, 0, 0], math.radians(90))

before.transform(R * S * T)

# ==============================================================================
# Remesh
# As of Nov, 2021, compas.geometry.trimesh_remesh is unavailable in native Rhino
# environment, so compas_cloud is used here.
# ==============================================================================

L = sum(before.edge_length(*edge) for edge in before.edges()) / before.number_of_edges()

if compas.is_rhino():
    from compas_cloud import Proxy
    proxy = Proxy()
    trimesh_remesh = proxy.function('compas.geometry.trimesh_remesh')
    V, F = trimesh_remesh(before.to_vertices_and_faces(), 3 * L)
else:
    V, F = cg.trimesh_remesh(before.to_vertices_and_faces(), 3 * L)

after = cd.Mesh.from_vertices_and_faces(V, F)

# ==============================================================================
# Viz
# ==============================================================================
box = cg.Box.from_bounding_box(before.bounding_box())
dx = 1.5 * box.xsize

if compas.is_rhino():
    import compas_ghpython.artists as artist
    a = artist.MeshArtist(before).draw_faces(join_faces=True)
    b = artist.MeshArtist(after.transformed(cg.Translation.from_vector([dx, 0, 0]))).draw_faces(join_faces=True)

else:
    from compas_view2.app import App
    viewer = App()  
    viewer.add(before)
    viewer.add(after.transformed(cg.Translation.from_vector([dx, 0, 0])))
    viewer.run()