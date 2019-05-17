# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from setuptools import find_packages, setup, Extension

with open('README.md') as f:
    readme = f.read()

with open('LICENCE') as f:
    licence = f.read()

setup(
    name='plum',
    version='0.1.0',
    description='Multiple dispatch in Python',
    long_description=readme,
    author='Wessel Bruinsma',
    author_email='wessel.p.bruinsma@gmail.com',
    url='https://github.com/wesselb/plum',
    license=licence,
    packages=find_packages(exclude=('tests', 'docs')),
    ext_modules=[Extension('plum.function',
                           ['plum/function.py'])])
