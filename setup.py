#!/usr/bin/env python

from setuptools import find_packages, setup


setup(
    name='txctools',
    description='Tools for TwistedChecker.',
    version='0.1.0',
    author='HawkOwl',
    author_email='hawkowl@outlook.com',
    url='https://github.com/hawkowl/txctools',
    packages=find_packages(),
    package_data={
        },
    scripts=[
        'bin/txc_hotspot',
        'bin/txc_json'
        ],
    license='MIT',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Quality Assurance"
        ],
    keywords=[
        "twistedchecker", "pylint", "txc"
        ],
    install_requires=[
        "twistedchecker"
        ],
    long_description=file('README.rst').read()
    )
