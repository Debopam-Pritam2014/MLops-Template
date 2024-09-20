import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.1"


REPO_NAME="MLops-Template"
AUTHOR_NAME="Debopam-pritam2014"
SRC_REPO="Firstproject"
AUTHOR_EMAIL='debopamdeycse19@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    long_description="MLOps Template for everyone.",
    Long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),

)
