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
      url="https://github.com/claymcleod/celcius/",
      download_url="https://github.com/claymcleod/celcius/tarball/0.0.1",
      scripts=['scripts/celcius-init', 'scripts/celcius-schedule', 'scripts/celcius-unschedule', 'scripts/celcius-status'],
      install_requires=['']
     )
