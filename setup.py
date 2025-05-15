from setuptools import setup, find_packages

setup(
    name="biolab",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'biopython>=1.81',
        'matplotlib>=3.5.0',
        'numpy>=1.21.0',
    ],
    author="kc-eng",
    author_email="your.email@example.com",
    description="A collection of bioinformatics programs",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kc-eng/biolab",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
) 