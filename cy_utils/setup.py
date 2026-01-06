from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

# Replacement for get_numpy_include_dirs()
include_dirs = [np.get_include()]

extensions = [
    Extension(
        "cy_utils",
        sources=["cy_utils.pyx"],
        include_dirs=include_dirs
    )
]

setup(
    ext_modules=cythonize(extensions),
)