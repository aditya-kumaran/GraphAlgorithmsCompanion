from setuptools import setup, find_packages

setup(
    name='GraphAlgorithmsCompanion',
    version='0.1',
    packages=find_packages(),  # Automatically finds your modules
    install_requires=['networkx'],  # Add other dependencies if needed
    author='Aditya Kumaran',
    description='Companion library for graph algorithms like DFS and Floyd-Warshall',
)
