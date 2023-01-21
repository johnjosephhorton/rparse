from setuptools import setup, find_packages

setup(
    name='rparse',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'rparse = rparse.rparse:main'
        ]
    },
    install_requires=[],
    description='A script that parses R script and returns info about csv files, libraries and outputs',
    author='John Horton',
    author_email='john.joseph.horton@gmail.com',
    url='https://github.com/johnjosephhorton/rparse'
)
