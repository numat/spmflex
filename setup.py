"""Python driver and command line tool for Honeywell SPM Flex gas detectors."""
from setuptools import setup

with open('README.md', 'r') as in_file:
    long_description = in_file.read()

setup(
    name="spmflex",
    version="0.1.1",
    description="Python driver for Honeywell SPM Flex gas dectectors.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="http://github.com/numat/spmflex/",
    author="Patrick Fuller",
    author_email="pat@numat-tech.com",
    packages=['spmflex'],
    install_requires=['aiohttp', 'xmltodict'],
    entry_points={
        'console_scripts': [('spmflex = spmflex:command_line')]
    },
    license='GPLv2',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces'
    ]
)
