from distutils.core import setup
import os

print(os.getcwd())

with open(
    'README.md', 
    encoding='utf-8'
) as file:
    description = file.read()

setup(
    name='yolo7',
    version='0.0.1',
    packages=["models", "utils", "deploy"],
)