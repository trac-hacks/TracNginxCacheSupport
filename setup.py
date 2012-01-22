#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from setuptools import setup

setup(
    name = 'TracNginxCacheSupport',
    version = '1.0',
    packages = ['nginxcachesupport'],

    author = 'Colin Snover',
    author_email = 'tracplugins@zetafleet.com',
    description = 'Add support for Nginx caching to Trac',
    long_description = 'A Trac plugin that sends X-Accel-Expires headers so Nginx < 0.8 can cache pages for unauthenticated users.',
    license = 'MIT',
    keywords = 'trac plugin nginx cache',
    classifiers = [
        'Framework :: Trac',
    ],
    
    install_requires = ['Trac'],
    
    entry_points = {
        'trac.plugins': [
            'nginxcachesupport = nginxcachesupport',
        ],
    }
)

