from setuptools import setup, find_packages

setup(
    name='Findupe',
    version='1.0',
    author='Saurabh Tiwari',
    packages=find_packages(),
    install_requires=['cv2'],
    description='Finding similar looking images using structural similarity',
    url='https://github.com/meispi/Findupe'
)