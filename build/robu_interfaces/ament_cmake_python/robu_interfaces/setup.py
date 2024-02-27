from setuptools import find_packages
from setuptools import setup

setup(
    name='robu_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('robu_interfaces', 'robu_interfaces.*')),
)
