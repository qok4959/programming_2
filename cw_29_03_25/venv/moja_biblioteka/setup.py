from setuptools import setup, find_packages

setup(
    name='moja_biblioteka',
    version='1.0',
    author='qok4959',
    packages=find_packages(),
    install_required=['numpy>=1.26', 'requests']
)