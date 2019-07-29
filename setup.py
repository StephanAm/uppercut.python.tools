from setuptools import setup,find_packages
print('A')
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