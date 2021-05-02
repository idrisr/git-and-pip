import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gitandpip",
    version="0.1.0",
    author="idrisr",
    author_email="idris.raja@gmail.com",
    description="It's pip... with git.",
    long_description=long_description,
    url="https://github.com/idrisr/git-and-pip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
