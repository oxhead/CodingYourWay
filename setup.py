import unittest

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class UnitTest(TestCommand):

    def initialize_options(self):
        TestCommand.initialize_options(self)
    
    def finalize_options(self):
        TestCommand.finalize_options(self)

    def run_tests(self):
        test_loader = unittest.TestLoader()
        test_suite = test_loader.discover('tests')
        runner = unittest.runner.TextTestRunner()
        runner.run(test_suite)


setup_options = dict(
    name='coding',
    description='Universal Command Line Environment for HAAS.',
    author='Chin-Jung Hsu',
    packages=find_packages(exclude=['tests*']),
    cmdclass={'test': UnitTest},
    license="Apache License 2.0",
)

setup(**setup_options)
