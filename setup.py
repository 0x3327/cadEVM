from setuptools import setup

setup(
    name='cadEVM',
    version='0.1',
    packages=['cadEVM'],
    install_requires=['click', 'eth-ape', 'radcad'],
    entry_points='''
        [console_scripts]
        cadEVM=cadEVM.generator:cli
    ''',
)
