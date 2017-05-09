#!/usr/bin/env python

PROJECT = 'mesonbuild_highlight_syntax'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Generator for syntaxis highlight files of The Meson Build System for misc text editors',
    long_description=long_description,

    author='RedSkotina',
    author_email='red.skotina@gmail.com',

    url='https://bitbucket.org/RedSkotina/mesonbuild-highlight-syntax',
    download_url='https://bitbucket.org/RedSkotina/mesonbuild-highlight-syntax/downloads',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff','meson'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'mesonbuild_highlight_syntax = mesonbuild_highlight_syntax.main:main'
        ],
        'mesonbuild_highlight_syntax.app': [
            'extract = mesonbuild_highlight_syntax.extract:Extract',
            #'generate = mesonbuild-highlight-syntax.generate:Generate',
        ],
    },

    zip_safe=False,
)