from setuptools import setup, find_packages
import subprocess

BATCH_FILE_PATH = "./batch/installscript.bat"
EXECUTABLE_PATH = "./additionals/wkhtmltopdf.exe"


def pakages_lister():
    with open("requirements.txt") as f:
        pakages = f.read().splitlines()
    return pakages

# for this app we need wkhtmltopdf to be already installed in the system
# to install it we need to run a batch scripts as follows



setup(
    name='certificate-formator',
    version='0.0.1',
    packages=find_packages(),
    author="Mohit Raj Rathor",
    author_email="mohitrajrathor@gmail.com",
    description="A certificate generator program in python",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mohitrajrathor/certificate-formator",
    install_requires=pakages_lister(),
    classifiers=[
        "Programming Language :: Python :: 3.11",
    ]
)


