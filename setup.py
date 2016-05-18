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

setup(name='zint',
      version='1.0',
      description='Python ctypes interface to libzint',
      long_description=read('README.rst'),
      url='http://github.com/jmptbl/python-zint',
      author='Aragon Gouveia',
      author_email='aragon@phat.za.net',
      packages=['zint'],
      keywords='zint ctypes',
      license='BSD',
      zip_safe=False)
