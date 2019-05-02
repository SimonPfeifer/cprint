import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="c-print",
    version="1.0.1",
    author="Simon Pfeifer",
    author_email="s.pfeifer@2012.ljmu.ac.uk",
    description="Small python package for printing text in different colours and typography.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SimonPfeifer/cprint",
    packages=['cprint']
)