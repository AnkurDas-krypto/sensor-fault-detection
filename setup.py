from setuptools import find_packages, setup 
from typing import List
import os

# def get_requirements()-> List[str]:
#     #requirement_list: List[str] = []
#     with open('requirements.txt') as f:
#         req = f.read().splitlines()
#     return req

def get_requirements()->List[str]:
    requirement_list:List[str] = []
    return requirement_list

get_requirements() 

setup(
    name = "sensor",
    version="0.0.1",
    author = "Ankur Das",
    author_email = "ankurdas8017@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements(),
)


