from setuptools import setup, find_packages

setup(
        name='datasnap',
        version='0.1.0',
        description='Directory snapshots.',
        author='Neil Hansen',
        package_dir={'datasnap': 'datasnap'},
        author_email='neil@amber.film',
        packages=find_packages(),
    )