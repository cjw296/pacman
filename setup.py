import os
from setuptools import setup, find_packages

base_dir = os.path.dirname(__file__)

setup(
    name='pacman',
    author='Chris Withers',
    author_email='chris@withers.org',
    description="Something like buildout, but different",
    url='https://github.com/cjw296/pacman',
    )
