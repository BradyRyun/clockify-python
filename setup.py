from setuptools import setup, find_packages

setup(
    name='clockify',  # Required
    version='0.0.4',  # Required
    author="Paulo Sergio dos Santo Junior",
    author_email="paulossjuniort@gmail.com",
    description="A lib to access the Clockify ",
 
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