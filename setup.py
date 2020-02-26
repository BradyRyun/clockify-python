from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='clockify',  # Required
    version='1.0.16',  # Required
    author="Paulo Sergio dos Santo Junior",
    author_email="paulossjuniort@gmail.com",
    description="A lib to access the Clockify API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/integration_seon/libs/application/clockify",
    packages=find_packages(),
    
    install_requires=[
        'requests'
    ],

    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    setup_requires=['wheel'],
    
)