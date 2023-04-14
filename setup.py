import re

from setuptools import find_packages
from setuptools import setup


def get_version():
    filename = "ExceptNotifier/__init__.py"
    with open(filename) as f:
        match = re.search(r"""^__version__ = ['"]([^'"]*)['"]""", f.read(), re.M)
    if not match:
        raise RuntimeError("{} doesn't contain __version__".format(filename))
    version = match.groups()[0]
    return version


def get_long_description():
    with open("README.md") as f:
        long_description = f.read()
        return long_description


version = get_version()


setup(
    name="ExceptNotifier",
    version="0.1.2",
    author="parkminwoo",
    author_email="parkminwoo1991@gmail.com",
    description="With Python's try-except statement, experience a significantly more flexible way to receive notifications.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/dsdanielpark/ExceptNotifier",
    packages=find_packages(exclude=[]),
    python_requires=">=3.6",
    install_requires=[],
    keywords="Exception, Python, Python Exception Alarm, Error notifications, Customizable notifications, Traceback management, Single line alarm",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    entry_points={"console_scripts": ["ExceptNotifier=ExceptNotifier.cli:main"]},
)