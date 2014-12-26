from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='InstPakg',
    version='1.0.0',

    description='Essential Program Installer',
    long_description=long_description,

    url='',

    author='Mozzo',
    author_email='',

    license='MIT',

    classifiers=[
		# 	3 - ALPHA, 4 - BETA, 5 - STABLE
        'Development Status :: 5 - Stable',

        'Intended Audience :: Users',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='install setuptools development',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=[''],

    extras_require = {
        '': [''],
    },

    package_data={
        'json': ['source/DEFAULT.json'],
    },

    entry_points={
        'console_scripts': [
            'InstPakg=source:main',
        ],
    },
)
