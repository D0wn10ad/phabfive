#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import phabfive
from setuptools import setup

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open("README.md") as f:
    readme = f.read()

with open("CHANGELOG.md") as f:
    changelog = f.read()

install_requires = [
    "anyconfig>=0.10.0",
    "appdirs",
    "docopt",
    "jinja2",
    "phabricator",
    "pyyaml",
]
tests_require = [
    "coverage",
    "flake8",
    "pytest",
    "tox",
]
docs_require = ["docs"]
download_url = f"https://github.com/dynamist/phabfive/tarball/v{phabfive.__version__}"

setup(
    name=phabfive.__name__,
    version=phabfive.__version__,
    description=phabfive.__doc__,
    long_description=f"{readme}\n\n{changelog}",
    long_description_content_type="text/markdown",
    author="Rickard Eriksson",
    author_email="rickard@dynamist.se",
    url=phabfive.__url__,
    download_url=download_url,
    zip_safe=False,  # Prevent creation of egg
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        "test": tests_require,
        "docs": docs_require,
    },
    packages=["phabfive"],
    entry_points={
        "console_scripts": [
            "phabfive = phabfive.cli:cli_entrypoint",
        ],
    },
    python_requires=">=3.9",
    classifiers=[
        # "Development Status :: 1 - Planning",
        # "Development Status :: 2 - Pre-Alpha",
        # "Development Status :: 3 - Alpha",
        "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        # "Development Status :: 6 - Mature",
        # "Development Status :: 7 - Inactive",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
    ],
    platforms=["OS Independent"],
    license="Apache License 2.0",
)
