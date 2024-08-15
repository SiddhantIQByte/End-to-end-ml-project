from setuptools import find_packages,setup

from typing import List

extra_e ='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        [req.replace("\n","") for req in requirements]

        if extra_e in requirements:
            requirements.remove(extra_e)

     
setup(
    name='Ml Project',
    version='0.1.0',
    description='Machine Learning Project',
    author='SidIQByte',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
