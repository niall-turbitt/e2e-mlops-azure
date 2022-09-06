from setuptools import find_packages, setup

setup(
    name="e2e_mlops_ado",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=0.1,
    description="",
    author=""
)
