from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A library with package'
LONG_DESCRIPTION = 'A library with package. Long disc'
# Setting up
setup(
    name="Library_python",
    version=VERSION,
    author="ThMeyerNeu (Meferko)",
    author_email="<egor767680@gmial.com>",
    description=DESCRIPTION,
    packages=find_packages("package1, package2, package3"),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Linux",
        "Operating System :: Microsoft :: Windows",
    ]
)