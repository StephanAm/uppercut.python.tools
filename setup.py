from setuptools import setup
print('A')
setup(
    name='uppercut',
    version='0.0.1',
    description='A library to handle common tasks for creating an Uppercut module in python',
    py_modules=['test'],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3"
        "Operating System :: OS Independent"
    ],
)