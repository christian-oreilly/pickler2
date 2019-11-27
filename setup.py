from setuptools import setup, find_packages

setup(
    name='pickler',
    version='1.0.0',
    license='bsd-3-clause',
    url='https://github.com/christian-oreilly/pickler2.git',
    author="Christian O'Reilly",
    author_email='christian.oreilly@gmail.com',
    description="Small package allowing to decorate a function so that it automatically pickle its results" +
                " and load it the next time it is called.",
    packages=find_packages(),    
    install_requires=["numpy"],
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
