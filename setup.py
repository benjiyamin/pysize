
import os
from setuptools import setup


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


def readlines(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as open_file:
        return [l.split("==")[0] for l in open_file.readlines()]


setup(
    name='pysize',
    version='0.1',
    author='benjiyamin, see AUTHORS.md',
    author_email='benjiyamin@gmail.com',
    description='PySize is a lightweight tool for converting quantities between defined units',
    license='GNU General Public License v3 (GPLv3), see LICENSE.md',
    keywords='units measurement conversion size',
    url='https://benjiyamin.github.io/pysize',
    packages=['pysize'],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python'
    ],
)
