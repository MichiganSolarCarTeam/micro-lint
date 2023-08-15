"""Install the `microLint` script."""
from setuptools import find_packages, setup


setup(
    name="microLint",
    version="1.3.9",
    author="Karam Alrawi",
    author_email="kaab@umich.edu",
    description="C and C++ linter for Microsystems devision.",
    url="https://github.com/MichiganSolarCarTeam/microLint",

    packages=find_packages(),
    entry_points="""
    [console_scripts]
    microLint=microLint.__main__:main
    """,
    install_requires=["click==6.2"],
)