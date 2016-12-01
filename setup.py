from setuptools import setup, find_packages
import os

import pgcryptoauth


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.rst')

setup(
    name='django-pgcryptoauth',
    version=pgcryptoauth.__version__,
    description='Django hasher for pgcrypto encoded passwords.',
    long_description=README,
    url='https://github.com/tomatohater/django-pgcryptoauth',
    author='Drew Engelson',
    author_email='drew@engelson.net',
    license='MIT',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    package_data={},
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
