from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='list-dataloaders',
    version='1.0.0',
    description='This package contains a pure-python class that wraps a list of dataloaders and allows to iterate over them in a random order.',
    py_modules=["Downloader"],
    packages=find_packages(include=['list_dataloaders', 'list_dataloaders.*']),
    classifiers={
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    },
    long_description = long_description,
    long_description_content_type = "text/markdown",
    install_requires = [
        "torch>=1.7"
    ],
    extras_require = {
        "dev" : [
            "pytest>=3.7",
        ],
    },
    url="https://github.com/MorenoLaQuatra/list-dataloaders",
    author="Moreno La Quatra",
    author_email="moreno.laquatra@gmail.com",
)