import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Kreusada",
    version="1.0.0",
    author="Kreusada",
    author_email="kreusadaprojects@gmail.com",
    description="Pypi project used for testing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kreusada/KreuTests",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    package_data={
        "": ["*.json", "*.rst", "*.txt", "*.yaml"]
    }
)