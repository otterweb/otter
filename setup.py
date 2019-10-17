import os
import re
import json
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

version = '0.0.1'


kwargs = {
        'name': 'otter',
        'version': version,
        'description': 'Python library for interacting with Otter Web API',
        'long_description':long_description,
        'packages': ['otter'],
        'zip_safe': False,
        }

setup(**kwargs)



