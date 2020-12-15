"""setup.py for Sofia2"""

from distutils.core import setup
import setuptools # pylint: disable=unused-import
from setuptools import find_packages


setup(
    name='Sofia2',
    version='0.0.1a',
    description='A simple, modular and fast smart-home system.',
    author='Marko Vejnovic',
    packages=find_packages()
)
