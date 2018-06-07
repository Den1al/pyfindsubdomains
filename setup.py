import os
from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name="pyfindsubdomains",
    version="0.0.2.3",
    author="@Daniel_Abeles",
    author_email="abeles22@gmail.com",
    description="This is a python3 wrapper to FindSubDomains",
    license="BSD",
    keywords="FindSubDomains, bruteforce, dns, subdomain",
    url='https://github.com/Den1al/pyfindsubdomains',
    packages=['findsubdomains'],
    long_description=readme(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking",
        "Topic :: System :: Networking :: Firewalls",
        "Topic :: System :: Networking :: Monitoring",
    ],
    install_requires=[
        'requests',
        'bs4'
    ],
    entry_points={
        'console_scripts': ['findsubdomains=findsubdomains.cli:main'],
    }
)
