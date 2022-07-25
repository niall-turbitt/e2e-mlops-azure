from setuptools import find_packages, setup
from e2e_mlops_ado import __version__

setup(
    name="e2e_mlops_ado",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="",
    author=""
)
