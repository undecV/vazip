import vazip
from setuptools import setup

setup(
    name='vazip',
    version=vazip.__version__,
    py_modules=['vazip'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        vazip=vazip:main
    ''',
)
