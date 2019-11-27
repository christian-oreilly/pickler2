from setuptools import setup, find_packages

setup(
    name='pickler',
    version='0.0.1',
    url='https://github.com/christian-oreilly/pickler.git',
    author="Christian O'Reilly",
    author_email='christian.oreilly@gmail.com',
    description="Small package allowing to decorate a function so that it automatically pickle its results" +
                " and load it the next time it is called.",
    packages=find_packages(),    
    install_requires=["numpy"],
)
