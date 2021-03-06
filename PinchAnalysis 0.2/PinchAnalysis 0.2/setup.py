#! /usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Name:
File Name: setup
Description: 
Category:
Requested Elements:
Requested Elements:
Author: Luis Eduardo Correa Gallego
Created on: 14/10/2018
Last modification: 
Used IDE: PyCharm Professional Edition
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PinchAnalysis",
    version="0.2",
    author="Luis Eduardo Correa Gallego",
    author_email="luise.correa@udea.edu.co",
    description="Heat integration - pinch analysis",
    keywords = "heat integration chemical engineering heat exchanger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LuisEduardoCorreaGallego/PinchAnalysis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
