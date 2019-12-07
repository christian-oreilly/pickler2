from setuptools import setup, find_packages

setup(
    name='pickler2',
    version='1.0.0',
    license='bsd-3-clause',
    url='https://github.com/christian-oreilly/pickler2.git',
    download_url="https://github.com/christian-oreilly/pickler2/archive/v1.0.0.tar.gz",
    author="Christian O'Reilly",
    author_email='christian.oreilly@gmail.com',
    description="Small package allowing to decorate a function so that it automatically pickle its results" +
                " and load it the next time it is called.",
    packages=find_packages(),    
    install_requires=["numpy", "setuptools"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development',
        'License :: OSI Approved',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)
