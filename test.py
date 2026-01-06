import os
import sys

print(f"Python version: {sys.version}")
print(f"Executable: {sys.executable}")

try:
    from osgeo import gdal
    # "VERSION_NUM" gives a clean integer (e.g., 3080000 for 3.8.0)
    # "RELEASE_NAME" gives the standard string (e.g., "3.8.4")
    v_name = gdal.VersionInfo("RELEASE_NAME")
    print(f"GDAL Core: OK (v{v_name})")
except ImportError as e:
    print(f"GDAL Core: FAILED ({e})")

try:
    import numpy
    print(f"NumPy: OK (v{numpy.__version__})")
except ImportError:
    print("NumPy: NOT FOUND (gdal_array requires NumPy)")

try:
    from osgeo import _gdal_array
    print("GDAL Array Binary: OK")
except ImportError as e:
    print(f"GDAL Array Binary: FAILED ({e})")
    
# Check if the DLL directory is in the PATH
lib_path = os.path.join(sys.prefix, 'Library', 'bin')
if lib_path in os.environ['PATH']:
    print(f"Path Check: OK ({lib_path} is in PATH)")
else:
    print(f"Path Check: WARNING ({lib_path} is NOT in PATH)")