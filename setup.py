import numpy as np
from setuptools import Extension, setup, find_packages


extensions = [
    Extension(
        "pygame_loads",
        ["src\utils\pygame_loads.py"],
        include_dirs=[np.get_include()],
    ),
]

setup(
    name="Shop Shop Manager",
    version="0.1.0",
    description="Turn-based management game.",
    # long_description=open("README.md").read(), # BUG: Does not work
    author="snoozleEmily",
    author_email="snoozlingemily@gmail.com",
    url="https://github.com/snoozleEmily/shop_shop_manager",
    license="GNU GENERAL PUBLIC LICENSE",
    install_requires=[
        "numpy>=1.18.0",
        "pygame>=2.0.0",
    ],
    packages=find_packages(),
    include_package_data=True,
    package_data={
        # Includes credits for free content used in the game
        "shop_shop_manager": ["assets/credits.md"],
    },
    python_requires=">=3.6",
)
