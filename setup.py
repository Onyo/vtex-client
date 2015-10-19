# coding=utf-8
import os
import sys
from setuptools import setup

import vtex_client


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]
if sys.argv[1] == 'develop':
    REQUIREMENTS += [i.strip()
                     for i in open("requirements-development.txt").readlines()]


setup(
    name="vtex_client",
    version=vtex_client.__version__,
    author="Onyo Inc (onyo.com)",
    author_email="backend@onyo.com",
    description="Client to consume the VTEX payment gateway API",
    license="MIT License",
    keywords="vtex_client",
    url="https://github.com/Onyo/vtex-client",
    packages=['vtex_client', 'tests'],
    namespace_packages=['vtex_client'],
    package_dir={'vtex_client': 'vtex_client'},
    install_requires=REQUIREMENTS,
    download_url="https://github.com/Onyo/vtex-client/tarball/master",
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Environment :: Plugins",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
)