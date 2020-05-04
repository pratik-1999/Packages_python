from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="distripy", 
    version="0.0.1",
    author="pandav_7",
    author_email="pratik_pandav28@outlook.com",
    description="A lightweight Statistical-Computing package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pratik-1999/Packages_python/tree/master/distripy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)