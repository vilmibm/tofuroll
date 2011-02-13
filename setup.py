from setuptools import setup
from tofuroll import get_version

setup(
    name='tofuroll',
    version=get_version(),
    url='http://github.com/nathanielksmith/tofuroll',
    description='A basic framework for creating command line applications',
    author='Nathaniel K Smith',
    author_email='nathanielksmith@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    packages=['tofuroll'],
)
