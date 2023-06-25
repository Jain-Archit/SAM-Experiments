from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(filePath: str) -> List[str]:
    """
        This function returns list of requriements
    """
    requirements = []
    with open(filePath) as fp:
        requirements = fp.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(name = "SAM_Experiments",
    version="0.0.1",
    author = "Archit",
    author_email= "archit1997delhi@gmail.com",
    packages= find_packages(exclude="notebooks"),
    install_requires = get_requirements("requirements.txt")   
    )