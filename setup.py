#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2012 Colin Snover
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from setuptools import setup

setup(
    name='TracNginxCacheSupport',
    version='1.0',
    packages=['nginxcachesupport'],

    author='Colin Snover',
    author_email='tracplugins@zetafleet.com',
    url='https://github.com/trac-hacks/TracNginxCacheSupport',
    description='Add support for Nginx caching to Trac',
    long_description="A Trac plugin that sends X-Accel-Expires headers "
                     "so Nginx < 0.8 can cache pages for unauthenticated "
                     "users.",
    license='3-Clause BSD',
    keywords='trac plugin nginx cache',
    classifiers=[
        'Framework :: Trac',
    ],
    install_requires=['Trac'],
    entry_points={
        'trac.plugins': [
            'nginxcachesupport = nginxcachesupport',
        ],
    }
)
