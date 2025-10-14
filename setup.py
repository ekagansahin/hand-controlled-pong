#!/usr/bin/env python3
"""Setup script for Hand-Controlled Pong Game."""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open(os.path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='hand-controlled-pong',
    version='1.0.0',
    author='ekagansahin',
    author_email='ekagansahin@users.noreply.github.com',
    description='A hand-controlled Pong game using MediaPipe hand tracking',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ekagansahin/hand-controlled-pong',
    py_modules=['pong_game'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Games/Entertainment :: Arcade',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'Environment :: X11 Applications',
        'Natural Language :: English',
    ],
    keywords='pong game hand-tracking mediapipe opencv pygame computer-vision gesture-control',
    python_requires='>=3.8',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'hand-pong=pong_game:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/ekagansahin/hand-controlled-pong/issues',
        'Source': 'https://github.com/ekagansahin/hand-controlled-pong',
        'Documentation': 'https://github.com/ekagansahin/hand-controlled-pong#readme',
    },
    include_package_data=True,
    zip_safe=False,
)

