from setuptools import setup
import setuptools

setup(name='travis_ci_tutorial',
      version='0.1',
      description='Example of python package for use with Travis CI',
      url='https://github.com/Lenijas/travis-ci-tutorial',
      author='Jaisiel Santana',
      author_email='jaisiel@gmail.com',
      license='',
      packages=['travis_ci_tutorial'],
      #packages=setuptools.find_packages(),

      entry_points={
        'console_scripts': [
            'travis-ci-tutorial = travis_ci_tutorial.src.tutorial:main',
        ]
      },
      zip_safe=False)