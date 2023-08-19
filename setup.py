import setuptools


with open('README.md', 'r', encoding='utf-8') as fl:
    long_description = fl.read()

setuptools.setup(
    name="FileCommands",
    version="0.0.1",
    author="Zhang",
    author_email="",
    description="supply some file commands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "zcopy=FileCommands:zcopy",
            "zmove=FileCommands:zmove",
            "zdel=FileCommands:zdel",
            "zrecycle=FileCommands:zrecycle",
            "zlist=FileCommands:zlist"
        ]
    },
    python_requires='>=3.7',
    install_requires=[
        'send2trash>=1.8.0',
    ]
)
