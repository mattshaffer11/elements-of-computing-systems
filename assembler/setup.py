from setuptools import setup

from codecs import open
from os import path

from setuptools import setup

BASE_PATH = path.abspath(path.dirname(__file__))


def read(filepath):
    with open(path.join(BASE_PATH, filepath), encoding='utf-8') as f:
        return f.read()


setup(
    name='hack',
    version='0.1',
    description='Hack assembler',
    long_description=read('README.rst'),
    license='MIT',
    py_modules=['hack'],
    author='Matt Shaffer',
    author_email='mattshaffer11@gmail.com',
    entry_points='''
        [console_scripts]
        hass=hack.cli:main
    '''
)
