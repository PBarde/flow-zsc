#!/usr/bin/env python3
# flake8: noqa
"""Setup script for the Flow repository."""
from os.path import dirname, realpath
from setuptools import find_packages, setup, Distribution
import setuptools.command.build_ext as _build_ext
import subprocess
from flow.version import __version__


def _read_requirements_file():
    """Return the elements in requirements.txt."""
    req_file_path = '%s/requirements.txt' % dirname(realpath(__file__))
    with open(req_file_path) as f:
        return [line.strip() for line in f]

class BinaryDistribution(Distribution):
    """See parent class."""

    def has_ext_modules(self):
        """Return True for external modules."""
        return True


setup(
    name='flow',
    version=__version__,
    distclass=BinaryDistribution,
    packages=find_packages(),
    description=("A system for applying deep reinforcement learning and "
                 "control to autonomous vehicles and traffic infrastructure"),
    long_description=open("README.md").read(),
    url="https://github.com/flow-project/flow",
    keywords=("autonomous vehicles intelligent-traffic-control"
              "reinforcement-learning deep-learning python"),
    install_requires=_read_requirements_file(),
    zip_safe=False,
)
