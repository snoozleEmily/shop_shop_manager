import numpy as np

from setuptools import Extension, setup, find_packages
from Cython.Build import cythonize


extensions = [
    Extension(
        "music",
        ["music.pyx"],
        include_dirs=[r"\Python311\site-packages\pygame"],
    ),
    Extension(
        "pygame_loads",
        ["pygame_loads.py"],
        include_dirs=[np.get_include()],
    ),
]

setup(
    name="Shop Shop Manager",
    version="0.1.0",
    description="Turn-based management game.",
    long_description=open("README.md").read(),
    author="snoozleEmily",
    author_email="snoozlingemily@gmail.com",
    url="https://github.com/snoozleEmily/shop_shop_manager",
    license="MIT",
    install_requires=[
        "numpy>=1.18.0",
        "pygame>=2.0.0",
        "cython>=0.29",
        # Note: A C/C++ compiler (e.g., MinGW on Windows)
        # is required to build Cython extensions.
    ],
    packages=find_packages(),
    include_package_data=True,
    package_data={
        # Includes credits for free content used in the game
        "shop_shop_manager": ["assets/credits.md"],
    },
    ext_modules=cythonize(extensions),
    python_requires=">=3.6",
)
