import os.path as P
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(P.join(P.dirname(__file__), 'requirements.txt')) as f:
    requires = f.read().splitlines()

setuptools.setup(
    name="dfreduce",
    version="1.2",
    author="Arun Nemani",
    author_email="neman014@gmail.com",
    test_suite='nose.collector',
    tests_require=['nose'],
    description="Automatic size reduction for pandas dataframe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arun-nemani/dfreduce",
    packages=setuptools.find_packages(),
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
