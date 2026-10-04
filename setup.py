'''Setup.py file is an essential part of packaging and distributing python projects . It is used by 
setuptools to define the configuration of your project , such as its metadata , dependences and more
'''
from setuptools import find_packages , setup
from typing import List

def get_requirements()->List[str]:
    '''This function will return list of requirements'''
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()

       
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

setup(
    name= "NetworkSecurity",
    version='0.0.1',
    author="Keshav Gupta",
    author_email="keshav10017@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements()
)