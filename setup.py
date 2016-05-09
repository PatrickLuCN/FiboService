from setuptools import setup, find_packages

setup(

    name="FiboService",
    version="0.1.0",
    author="Patrick Lu",
    author_email="Patrick.MG.Lu@gmail.com",
    package=find_packages(),
    include_package_data=True,
    url="http://pypi.python.org/pypi/xxxx",
    license="LGPL",
    description="A simple RESTful service for fibonacci-number calculation",
    install_requires=[
        "flask",
    ],
)

