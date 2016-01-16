#!/usr/bin/env python
__version__ = '0.1'

from setuptools import setup, find_packages

setup(name='celcius',
      version=__version__,
      description='Wrapper for data pipelining using UNIX microservices',
      author='Clay McLeod',
      author_email='clay.l.mcleod@gmail.com',
      package_dir={ '': 'lib' },
      packages=find_packages('lib'),
      scripts=['scripts/celcius', 'scripts/celcius-init', 'scripts/celcius-schedule'],
      install_requires=['']
     )
