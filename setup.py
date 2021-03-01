from setuptools import setup

setup(
name='biospacy',
version='0.0.2',
description = 'The package is text labeling function.',
url = 'git+ssh://git@github.com/Nyaribari/biospaCy#egg=labels',
author='Nyarbari Reuben',
author_email='anyaribari@gmail.com',
licence='unlicense',
packages=['biospacy'],
install_requires=['spacy','pandas'],
zip_safe= False
)