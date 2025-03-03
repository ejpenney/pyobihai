"""PyObihai Setup."""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyobihai",
    version="1.4.2",
    author="Emory Penney",
    author_email="treadstoneit@gmail.com",
    description="A Python wrapper for Obihai",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ejpenney/pyobihai",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
        "defusedxml",
    ],
)
