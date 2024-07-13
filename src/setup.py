from setuptools import Extension, setup
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension(
        "music", ["music.pyx"],
        include_dirs=[r"\Python311\site-packages\pygame"],         
        ),
    Extension(
        "market_board", ["market_board.py"],
        include_dirs=[np.get_include()],         
        ) 
]
setup(
    ext_modules = cythonize(extensions)
)

