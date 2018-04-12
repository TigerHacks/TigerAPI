'''
SPDX-License-Identifier: MIT

Install ghdata package with pip.
'''

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='thapi',
    version='0.0.1',
    include_package_data = True,
    description='API for TigerHacks',
    long_description=long_description,
    url='tiger-hacks.com',
    author='Christian Cmehil-Warn',
    author_email='cmehil.warn@gmail.com',
	packages=['thapi'],
	package_dir={'thapi': 'thapi'},
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='ghtorrent github api data science',
    install_requires=['ipdb', 'setuptools-git', 'beautifulsoup4', 'flask', 'flask-cors', 'PyMySQL', 'requests', 'python-dateutil', 'sqlalchemy', 'pandas', 'pytest', 'pyevent', 'gunicorn'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    entry_points={
        'console_scripts': [
            'thapi=thapi.server:run',
        ],
    },
)
