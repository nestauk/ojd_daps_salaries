from setuptools import setup, find_packages
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Function to read the contents of the requirements.txt file

def read_lines(path):
    """Read lines of `path`."""
    with open(path) as f:
        return f.read().splitlines()

setup(
    name='ojd_daps_salaries',
    description="Annualises salaries from online job adverts",
    long_description=open(BASE_DIR / "README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    version='0.1.0',
    install_requires=read_lines(BASE_DIR / "requirements.txt"),
    packages=find_packages(
        exclude=["docs", "tests"]
    ),
    classifiers=["Development Status :: 5 - Production/Stable"],
    package_data={
        # If any package contains *.yaml files, include them:
        "": [
            "*.yaml",
        ],
    },
    url="https://github.com/nestauk/ojd_daps_salaries",
    project_urls={
        "Documentation": "https://nestauk.github.io/ojd_daps_salaries/index.html",
        "Source": "https://github.com/nestauk/ojd_daps_salaries",
    },
    author="Nesta",
    author_email="dataanalytics@nesta.org.uk",
    maintainer="Nesta",
    maintainer_email="dataanalytics@nesta.org.uk",
    license="MIT",
)
