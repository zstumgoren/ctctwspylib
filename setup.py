#!/usr/bin/env python
from distutils.core import setup

setup(name='ctctwspylib',
      version='0.1.1a1',
      description='A clone of the original lib from SourceForge (https://sourceforge.net/projects/ctctwspylib/)',
      author='Serdar Tumgoren',
      author_email='zstumgoren@gmail.com',
      url='https://github.com/zstumgoren/ctctwspylib',
      license='Apache 2.0',
      packages=['ctctwspylib'],
      install_requires=['csvkit'],
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License 2.0',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries',
      ]
)
