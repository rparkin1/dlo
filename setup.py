"""Setup module for the liteflow package."""

from setuptools import setup, find_packages

setup(name='dlo',
      version='0.0.1',
      description='Deep Knowledge Extraction from Text',
      url='https://github.com/rparkin1/dlo.git',
      packages=find_packages(exclude=["tests"]),
      install_requires=[
          'editdistance==0.3.1',
          'liteflow==0.1.0',
          'six==1.10.0',
          'edit-distance==1.0.0'
          
      ],
      dependency_links=[
          'git+https://github.com/petrux/LiTeFlow.git@master#egg=liteflow-0.1.0'
      ],
      zip_safe=False)
