from setuptools import setup, find_packages


setup(
    name='snapshot',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'snapshot = monitoring.snapshot:main',
        ],
    },
    install_requires=[
        'psutil',
        'argparse'
    ],
    version='0.1',
    author='Raman Rohau',
    author_email='raman_rohau@epam.com',
    description='Logging information about CPU, Memory, Disk and Network usage'
)
