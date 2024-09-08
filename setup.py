# Remain Common in every Project
# I will use it as local package

import setuptools

# IMAGE Seeker Package in pypi

with open("README.md","r",encoding="utf-8") as f: # Open in write mode
    long_description=f.read()

__version__="0.0.0"

REPO_NAME= "Text_Summarization"
AUTHOR_USER_NAME="PriyanshuDey23"
SRC_REPO= "Text_Summarization"
AUTHOR_EMAIL="priyanshudey.ds@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="It is a NLP Problem Statement",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/PriyanshuDey23/Text_Summarization",
    project_urls={
        "Bug Tracker":f"https://github.com/PriyanshuDey23/Text_Summarization"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")



)