import setuptools

setuptools.setup(
    name='huy',    
    version="0.1",

    author="manatlan",
    author_email="manatlan@gmail.com",
    description="Like python eel, but for py3, with asyncio",
    long_description=open("README.md","r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/manatlan/reqman",
    py_modules=["huy"], #setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ),
    install_requires=[
          'aiohttp',
    ],    
)