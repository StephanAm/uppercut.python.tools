from setuptools import setup,find_packages
from sys import argv
import json

with open('.version','r') as f:info = json.load(f)

if True or 'step' in argv:
    print('stepping version')
    info['version'][-1] = info['version'][-1]+1
    with open('.version','w') as f:json.dump(info,f)

print(info)

setup(
    name='uppercut',
    url='https://github.com/StephanAm/uppercut.python.tools',
    author='Stephan Marais',
    maintainer='Stephan Marais',
    version='0.0.9',
    description='A library to handle common tasks for creating an Uppercut module in python.',
    py_modules=['test'],
    package_dir={'':'src'},
    packages=find_packages('src'),
    classifiers=[
        "Programming Language :: Python :: 3.7"
    ],
    install_requires = [
        'redis'
    ]
)