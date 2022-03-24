from setuptools import setup, find_packages

setup(
    name='WebSafer',
    version='0.1.0',
    packages=find_packages(include=['WebSafer', 'WebSafer.*']),
    url='https://github.com/IsaiahStanke/WebSafer',
    license='GNU General Public License v3.0',
    author='Isaiah Stanke',
    author_email='',
    description='A tool that blocks websites on single computer\'s to make the Web safer'
)
