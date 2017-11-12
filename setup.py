# Kinesis Aggregation/Deaggregation Libraries for Python
#
# Copyright 2014, Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Amazon Software License (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
# http://aws.amazon.com/asl/`
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

import os.path

from setuptools import setup


def read_file(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, 'r') as source_file:
        return source_file.read()


setup(
    name='kinaggregator',
    packages=['kinaggregator'],
    version='0.1.2',
    description='Python module to assist in taking advantage of the Kinesis message aggregation format for both aggregation and deaggregation. Based on aws_kinesis_agg.',
    long_description=read_file('README.md'),
    author='Darko Ronic',
    author_email='darko.ronic@gmail.com',
    license='SEE LICENSE IN LICENSE',
    url='http://github.com/apolloFER/kinaggregator',
    keywords=['aws', 'kinesis', 'aggregation', 'deaggregation', 'kpl'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    install_requires=[
        'protobuf',
        'six'
    ]
)
