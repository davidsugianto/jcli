from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='jcli',
    version='0.1',
    author='David Sugianto',
    author_email="idiots718@gmail.com",
    description="jcli is a jogjacode CLI tools for automation using python and ansible",
    long_description=readme(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        jcli=jcli.main:cli
    ''',
)