import setuptools


with open('README.md', 'r', encoding='utf-8') as fl:
    long_description = fl.read()

setuptools.setup(
    name="FileCommands",
    version="0.0.1",
    author="Zhang",
    author_email="",
    description="supply some file commands for different system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "zcopy=FileCommands:zcopy",
            "zmove=FileCommands:zmove",
            "zdel=FileCommands:zdel"
        ]
    },
    # python_requires='>=3.8.6',
    # install_requires=[
    #     'bs4>=0.0.1',
    # ]
)