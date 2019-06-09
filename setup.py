import codecs
import os
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()

def description():
    """
Python-Zint is a ctypes interface to libzint of Robin Stuart's Zint project:

<http://www.zint.org.uk/> <https://zint.github.io>

Usage closely follows the C API:

<http://www.zint.org.uk/Manual.aspx?type=p&page=5>
    """
    pass

setup(name='zint',
      version='1.2',
      description='Python ctypes interface to libzint',
      long_description=description.__doc__.strip(),
      url='http://github.com/jmptbl/python-zint',
      author='Aragon Gouveia',
      author_email='aragon@phat.za.net',
      packages=['zint'],
      keywords='zint ctypes',
      license='BSD',
      zip_safe=False)
