"""Setup for the conceal package."""

import setuptools


with open("README.md") as f:
    README = f.read()

setuptools.setup(
    author="Michael Peters",
    author_email="michaelpeterswa@icloud.com",
    name="conceal",
    license="MIT",
    description="conceal is a camouflage generator.",
    version="v1.0.0",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/michaelpeterswa/conceal",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
