from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirments(file_path:str)->List[str]:
    '''this function will return the list of requirements'''
    requirmentss=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]

        if HYPHEN_E_DOT in requirments:
            requirments.remove(HYPHEN_E_DOT)

    return requirments

    
setup(
name='mlproject',
version='0.0.1',
author='AMNUJK',
author_email='av862064@student.nitw.ac.in',
packages=find_packages(),
install_requires=get_requirments('requirements.txt')

)