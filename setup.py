import setuptools

setuptools.setup(
    name='WebSafer',
    version='0.1.0',
    packages=setuptools.find_packages(),
    url='https://github.com/IsaiahStanke/WebSafer',
    license='GNU General Public License v3.0',
    author='Isaiah Stanke',
    author_email='',
    description='A tool that blocks websites on single computer\'s to make the Web safer',
    install_requires=['lib2to3.pytree', 'colorama', 'shutil', 'pathlib']
)
