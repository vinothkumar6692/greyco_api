
# -*- coding: utf-8 -*-
#
# @Author: Vinoth Kumar
# @Email:   vinothkumar@nyu.edu

from setuptools import setup, find_packages

## Get our requirements from our .txt file
with open('requirements.txt') as requirements:
	modules = [line.strip('\n') for line in requirements]

setup(name = 'greystone',
	version = '0.1',
	description = 'A simple Django Rest API',
	author = 'Vinoth Kumar',
	author_email = 'vinothkumar@nyu.edu',
	install_requires = modules
)