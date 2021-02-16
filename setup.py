import setuptools

setuptools.setup(
    name="RPGenerator",
    version="1.0.0",
    description="A random monster generator",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'})