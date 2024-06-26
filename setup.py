from setuptools import setup, find_packages
from typing import List


# Declaring variables for set functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.5"
AUTHOR = "Swadhika Mishra"
DESCRIPTION = "This is a first FSDS nov batch Machine learning project"
REQUIREMENT_FILE_NAME = 'requirements.txt'


def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file

    return this function is going to return list which contain 
    name of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
    # name = "housing-predictor"
    # version = "0.0.1"
    # author = "Swadhika Mishra"
    # description = "This is a first FSDS nov batch Machine learning project"

    name = PROJECT_NAME, 
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = find_packages(),
    install_requires = get_requirements_list()
)
