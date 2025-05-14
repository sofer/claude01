"""Setup file for the FAC command line tool."""

from setuptools import setup, find_packages

setup(
    name="fac",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "fac=fac.cli:main",
        ],
    },
    python_requires=">=3.6",
)