from setuptools import setup, find_packages
import os

# Function to read the requirements.txt
def read_requirements(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

# Read the requirements from InternVideo2/multi_modality/requirements.txt
requirements = read_requirements('requirements.txt')

setup(
    name='InternVideo2',
    version='0.0.1',
    description='InternVideo2 model pip package',
    packages=find_packages(where='InternVideo2'),
    package_dir={'': 'InternVideo2'},
    install_requires=requirements,
    include_package_data=True,
    package_data={
        '': ['*.txt', '*.md', '*.cfg', '*.json'],
    },
)
