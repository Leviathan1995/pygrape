#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    # Use setuptools if available, for install_requires (among other things).
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pygrape',
    packages=['pygrape'],
    version='1.1',
    description='pygrape is a python library for updating terminal output in realtime',
    long_description=open('README.md').read(),
    author='leviathan1995',
    author_email='leviathan0992@gmail.com',
    url='https://github.com/Leviathan1995/pygrape',
    license='MIT',
)
