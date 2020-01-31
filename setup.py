import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="climateserv", # Replace with your own username
    version="0.0.1",
    author="Billy Ashmall",
    author_email="billy.ashmall@nasa.gov",
    description="This is a simple package to access the ClimateSERV API",
    long_description=long_description,
    long_description_content_type="This is a simple package to access the [ClimateSERV API](https://climateserv.servirglobal.net/) ",
    url="https://github.com/servir/ClimateSERVpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['urllib', 'urllib.request', 'json', 'configparser', 'logging', 'csv'],
)