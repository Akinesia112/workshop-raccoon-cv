"""
Get the path of files in the same folder with this GH file.
If filename is omitted, this will return the path of this GH file.
"""

import Grasshopper
import os

filepath = ghenv.Component.OnPingDocument().FilePath
path = os.path.dirname(filepath)
if filename is not None:
    path = os.path.join(path, *filename)
