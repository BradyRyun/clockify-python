from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='clockify',  # Required
    version='3.0.1',  # Required
    author="New: Brady Ryun, Original: Paulo Sergio dos Santos Junior",
    author_email="brady@ryunengineering.com",
    description="Clockify is the only truly free time tracker and timesheet app for teams of all sizes. Unlike all the other time trackers, Clockify is available for an unlimited numbers of users for free",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BradyRyun/clockify-python",
    packages=find_packages(),
    
    install_requires=[
        'requests', 'factory_boy'
    ],

    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    setup_requires=['wheel'],
    
)


