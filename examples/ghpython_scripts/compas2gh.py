"""Convert compas geometry to Rhino geometry.

This script is a gh_python component script.
A grasshopper python component needs to be set as follow:

input parameters
----------
* compas_geometry: no type hint, item access

output parameters
----------
* rhino_geometry
"""

import compas.datastructures as cd
import compas.geometry as cg
import compas_ghpython.artists as cgha
import compas
import Rhino.Geometry as rg  # type: ignore #noqa: F401

__author__ = 'ChiaChing Yen'
__email__ = '<ccyen@umich.edu>'


def convert_compas_geometry_to_gh_geometry(compas_geometry):
    """Converts a Rhino point to a COMPAS point.

    Parameters
    ----------
        rhino_point (Any): The rhino geometry that will be converted

    Returns:
    ----------
        compas.geometry
    """
    if isinstance(compas_geometry, cg.Point):
        return cgha.PointArtist(compas_geometry).draw()
    elif isinstance(compas_geometry, cg.Vector):
        return rg.Vector3d(compas_geometry.x, compas_geometry.y, compas_geometry.z)
    elif isinstance(compas_geometry, cg.Line):
        return cgha.LineArtist(compas_geometry).draw()
    elif isinstance(compas_geometry, cg.Frame):
        return cgha.FrameArtist(compas_geometry, scale=100).draw()
    elif isinstance(compas_geometry, cg.Plane):
        return cgha.FrameArtist(cg.Frame.from_plane(compas_geometry), scale=100).draw()
    elif isinstance(compas_geometry, cd.Mesh):
        return cgha.MeshArtist(compas_geometry).draw()
    elif isinstance(compas_geometry, cg.Polyline):
        return cgha.PolylineArtist(compas_geometry).draw()
    else:
        print("{0} is not supportted.".format(type(compas_geometry)))
        raise TypeError


if __name__ == "__main__":
    if compas.is_ironpython or compas.is_mono:
        if compas_geometry is not None:  # type: ignore # noqa: F823
            rhino_geometry = convert_compas_geometry_to_gh_geometry(compas_geometry)  # type: ignore # noqa: F823
