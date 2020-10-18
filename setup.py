#! /usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colorlib_gen",
    version="1.1.0",
    author="Oliver \"c0rp3n\" Hitchcock",
    author_email="",
    description="Generates a color map for ColorLib.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/c0rp3n/colorlib-gen",
    packages= ['colorlib_gen'],
    entry_points= {
        'console_scripts': [
            'colorlib_gen = colorlib_gen.__main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3 License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)
