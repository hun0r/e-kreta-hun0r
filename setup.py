from setuptools import setup, find_packages

setup(
    name="e_kreta",
    version="0.1",
    author="hunor, ferivoq",
    description="A Python API for interacting with the eKreta system.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/hun0r/e-kreta",
    packages=find_packages(),
    install_requires=[
        "requests",
        "PyJWT",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
