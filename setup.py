#!/usr/bin/env python

from setuptools import setup, find_packages
import re
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

name = "Noordsestern"

version_regex = r"^v(?P<version>\d*\.\d*\.\d*$)"
version = os.environ.get('CI_COMMIT_TAG', f'1.{os.environ.get("CI_COMMIT_REF_NAME","4.0")}')
full_version_match = re.fullmatch(version_regex, version)
if full_version_match:
    version = full_version_match.group('version')

setup(
    name="robotframework-zeebe",
    version=version,
    description="Keywords for camunda cloud.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=name,
    author_email="markus.i.sverige@googlemail.com",
    url="https://github.com/MarketSquare/robotframework-zeebe",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Framework :: Robot Framework",
    ],
    license="Apache License, Version 2.0",
    install_requires=["robotframework", "zeebe-grpc"],
    include_package_data=True,
)
