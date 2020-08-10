import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='django_sourcerer',
    version='2.1',
    author='Cem Arslan, Kadir Kocak, Ugur Dogus Hamarat, Cagatay Em, Farid Murmadov, Burak Karaca',
    author_email="cmarslan06@gmail.com",
    description="Django app that import and correlating data from external sources.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nokia-wroclaw/innovativeproject-django-sourcerer",
    packages=setuptools.find_packages(),
    install_requires=[
        'django == 3.0.5',
        'djangorestframework == 3.11.0',
        'requests == 2.23.0',
        'pyyaml == 5.3.1',
        'pandas == 1.0.3',
        'pytest == 5.4.1',
        'requests-mock == 1.7.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
