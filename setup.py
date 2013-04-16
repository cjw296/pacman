import os
from setuptools import setup, find_packages
from pacman.zdist import zdist

base_dir = os.path.dirname(__file__)

setup(
    name='pacman',
    author='Chris Withers',
    author_email='chris@withers.org',
    description="Something like buildout, but different",
    url='https://github.com/cjw296/pacman',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    cmdclass={'zdist': zdist}
    )
